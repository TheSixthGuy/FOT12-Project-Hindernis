#!Main.py
import RPi.GPIO as GPIO #Libary für die Benutzung von den GPIO-Pins
import time             #Libary für Zeit-basierte Funktionen
import smbus            #Libary für die benutzung des Datenbus-System I2C für das gyroscope
import math             #Libary für Mathe Funktion wie z.B Wurzel von
import random           #Libary für zufällige Nummern

#GPIO.setwarnings(False) #Ausschalten der Warnmeldung der GPIO-Pins
GPIO.setmode(GPIO.BCM)	 #Einschalten in das Breadboard-Pin system

gefundenG = False   #Gewicht gefunden Bool(True or False)
gefundenH = False   #Hindernis gefunden Bool
verlorenH = False   #Hindernis verloren Bool
gefundenZ = False   #Ziel gefunden Bool
drehenF = False     #Drehen Fertig Bool

static Lenkung = 1  #Statische(?) Varibale für die Lenkung 1 = voll rechts, -1 = voll links
power1 = 0x6b       #Hexadezimaladresee für den Strom des gyroscope
power2 = 0x6c       #?
TrigA = 23          #Varibale TRIGGER ist GPIO-Pinnummer für das Auslösen des US-Sensors
EchoA = 24          #Varibale Echo ist die GPIO-Pinnummer für den Pin des Echos/Output des Us-Sensors
TrigB = 17          #
EchoB = 27          #
bus = smbus.SMBus(1)    #Starten des Datenbus-System für das Gyroscope
address = 0x68 #Hexadezimaladresee des Gyroscope 

GPIO.setup(TrigA,GPIO.OUT)    #init der Pins
GPIO.setup(EchoB, GPIO.IN)    #
GPIO.setup(TrigB,GPIO.OUT)    #init der Pins
GPIO.setup(EchoB, GPIO.IN)    #
MotorA1 = GPIO.PWM(25, 50)                #Pins der Motoren festlegen und Frequenz
MotorB1 = GPIO.PWM(7, 50)                 #
MotorC1 = GPIO.PWM(10, 50)                #
MotorA2 = GPIO.PWM(8, 50)                 #
MotorB2 = GPIO.PWM(12,50)                 #
MotorC2 = GPIO.PWM(9, 50)                 #

MotorA1.start(0)    #Starten der Motoren ohne Drehung
MotorA2.start(0)    #
MotorB1.start(0)    #
MotorB2.start(0)    #
MotorC1.start(0)    #
MotorC2.start(0)    #

Vorwaerts(10)
while gefundenG = False:    #Suchen des Gewichts, wenn Gewicht näher als 5cm aufhören von Fahren
    if DistanzA() < 5:
        Stop()
        gefundenG = True

Greifen(10)  #Greifen des Gewichts
Vorwaerts(20) #Zum hindernis fahren
while gefundenH = False:   #Der Seitliche ultraschall-sensor schaut nach dem Hindernis und speichert die Entfernung
    if DistanzB() < 40:
        HindernisDistanz = DistanzB()
        gefundenH = True

while verlorenH = False:   #Der Seitliche US-Sensor gibt an wenn er das Hindernis nicht mehr sieht, Fahrzeug fährt 2sek weiter und stoppt 
    if DistanzB() > HindernisDistanz + 10:
        time.sleep(2)
        Stop()
        verlorenH = True

bus.write_byte_data(address,power1,0) 	#der gyroscope wird initalisiert
#TODO Gyro
GyX = wordLesen_2c(0x43) #Die ausgabe der X-Achse des Gyros wird gelsesen
StartX = GyX / 131  #(?) Wird in Grad umgerechnet

if random.randint(0,1) = 1: #Temp Spaß-Funktion Munz-Wurf zum auswählen der Dreh-Methode
	Kurve() #
else:
	DrehenStelle(30)

while drehenF = False:
	if (StartX - wordLesen_2c(0x43)) > 90:
		Stop()
		drehenF = True

Vorwaerts(20)
while gefundenZ = False:
	if DistanzA() < 50:
		Stop()
		gefundenZ = True

Loslassen()

MotorA2.stop
MotorB1.stop
MotorB2.stop
MotorC1.stop
MotorC2.stop
GPIO.cleanup                  #
print("Cleanup")

def Vorwaerts(KraftV):
    MotorA1.ChangeDutyCycle(KraftV)
    MotorB2.ChangeDutyCycle(KraftV)
    
def Rueckwaerts(KraftR):
    MotorA2.ChangeDutyCycle(KraftR)
    MotorB2.ChangeDutyCycle(KraftR)

def DrehenStelle(KraftD):
	MotorA1.ChangeDutyCycle(KraftD)
	MotorB2.ChangeDutyCycle(KraftD)

def Kurve():
	MotorA1.ChangeDutyCycle((((1/3)*(Lenkung**3))-(0.5*(Lenkung**2))+((2/3)*Lenkung)+0.5)*100)
	MotorB1.ChangeDutyCycle((((-1/3)*(Lenkung**3))-(0.5*(Lenkung**2))-((2/3)*Lenkung)+0.5)*100)
	
def Stop():
    MotorA1.ChangeDutyCycle(0)
    MotorA2.ChangeDutyCycle(0)
    MotorB1.ChangeDutyCycle(0)
    MotorB2.ChangeDutyCycle(0)
    
def Greifen(KraftG):
    MotorC2.ChangeDutyCycle(0)
    MotorC1.start(KraftG)
    time.sleep(2)
    
def Loslassen(KraftL):
    MotorC1.ChangeDutyCycle(0)
    MotorC2.start(KraftL)
    time.sleep(2)
    MotorC2.ChangeDutyCycle(0)
    
def DistanzA:
    
    GPIO.output(TrigA, GPIO.LOW) #Erholungszeit für den Sensor? (Wird eindeutig noch verändert9
    print ("Warten...")
    time.sleep(2)
    
    GPIO.output(TrigA, GPIO.HIGH) #Auslösen des US-Sensor für ein Bruchteil einer Sekunde
    time.sleep(0.00001)
    GPIO.output(TrigA, GPIO.LOW)
    
    while GPIO.input(EchoA)==0:      #zeitpunkt des Auslösen festnehemn
        Puls_Start = time.time()
        
    while GPIO.input(EchoA)==1:      #Zeitpunkt der Aufnahme des Echos
        Puls_EndeA = time.time()
                     
    Puls_DauerA = Puls_EndeA - Puls-StartA  #Ausrechnen der zeit differenz zwischen auslösen und des Echo
                     
    DistanzA = Puls_DauerA * 17150        #Ausrechnen der Distanz anhand zeitdifferenz * Schallgeschwindigkeit 
    DistanzA = round(DistanzA, 2)         #runden des Ergebnis auf 2 nachkommastellen
    return DistanzA

def DistanzB:

    GPIO.output(TrigB, GPIO.LOW) #Erholungszeit für den Sensor? (Wird eindeutig noch verändert9
    print ("Warten...")
    time.sleep(2)
    
    GPIO.output(TrigB, GPIO.HIGH) #Auslösen des US-Sensor für ein Bruchteil einer Sekunde
    time.sleep(0.00001)
    GPIO.output(TrigB, GPIO.LOW)
    
    while GPIO.input(EchoB)==0:      #zeitpunkt des Auslösen festnehemn
        Puls_Start = time.time()
        
    while GPIO.input(EchoB)==1:      #Zeitpunkt der Aufnahme des Echos
        Puls_EndeB = time.time()
                     
    Puls_DauerB = Puls_EndeB - Puls-StartB  #Ausrechnen der zeit differenz zwischen auslösen und des Echo
                     
    DistanzB = Puls_DauerB * 17150        #Ausrechnen der Distanz anhand zeitdifferenz * Schallgeschwindigkeit 
    DistanzB = round(DistanzB, 2)         #runden des Ergebnis auf 2 nachkommastellen
    return DistanzA

def byteLesen(reg):
    return bus.read_byte_data(address, reg)
    
def wordLesen(reg):
    high = bus.read_byte_data(address, reg)

def wordLesen_2c(reg):
    wert = wordLesen(reg)
    if (wert >= 0x8000):
        return -((65535 - wert) + 1)
    else:
        return wert
        
def distanz(a,b):
    return math.sqrt((a*a)+(b*b))
    
def get_y_rotation(x,y,z):
    radien = math.atan2(x, distanz(y,z))
    return -math.degrees(radien)
    
def get_x_rotation(x,y,z):
    radien = math.atan2(y, distanz(x,z))
    return math.degrees(radien)