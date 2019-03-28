!Main.py
import RPi.GPIO as GPIO
import time
import smbus
import math

#GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

gefundenG = False
gefundenH = False
verlorenH = False
gefundenZ = False

power1 = 0x6b
power2 = 0x6c
TrigA = 23                    #Varibale TRIGGER ist GPIO-Pinnummer für das Auslösen des US-Sensors
EchoA = 24
TrigB = 17
EchoB = 27
bus = smbus.SMBus(1)
address = 0x68

GPIO.setup(TrigA,GPIO.OUT)    #init der Pins
GPIO.setup(EchoB, GPIO.IN)
GPIO.setup(TrigB,GPIO.OUT)    #init der Pins
GPIO.setup(EchoB, GPIO.IN)
MotorA1 = GPIO.PWM(25, 50)                #GPIO-PIN-Nummer der Motoren in deren variable speichern
MotorB1 = GPIO.PWM(7, 50) 
MotorC1 = GPIO.PWM(10, 50)
MotorA2 = GPIO.PWM(8, 50)
MotorB2 = GPIO.PWM(12,50)
MotorC2 = GPIO.PWM(9, 50)

MotorA1.start(0)
MotorA2.start(0)
MotorB1.start(0)
MotorB2.start(0)
MotorC1.start(0)
MotorC2.start(0)

Vorwärts(10)
while gefundenG = False:
    if DistanzA() < 5:
        Stop()
        gefundenG = True

Greifen(10)
Vorwärts(20)
while gefundenH = False:
    if DistanzB() < 40:
        HindernisDistanz = DistanzB()
        gefundenH = True

while verlorenH = False:
    if DistanzB() > HindernisDistanz + 10:
        time.sleep(2)
        Stop()
        verlorenH = True

bus.write_byte_data(address,power1,0)
#TODO Gyro



MotorA2.stop
MotorB1.stop
MotorB2.stop
MotorC1.stop
MotorC2.stop
GPIO.cleanup                  #
print("Cleanup")

def Vorwärts(KraftV):
    MotorA1.ChangeDutyCycle(KraftV)
    MotorB2.ChangeDutyCycle(KraftV)
    
def Rückwärt(KraftR):
    MotorA2.ChangeDutyCycle(KraftR)
    MotorB2.ChangeDutyCycle(KraftR)

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