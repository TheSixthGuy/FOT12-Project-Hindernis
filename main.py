#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO #Libary für die Benutzung von den GPIO-Pins
import time             #Libary für Zeit-basierte Funktionen
import smbus            #Libary für die benutzung des Datenbus-System I2C für das gyroscope
import math             #Libary für Mathe Funktion wie z.B Wurzel von
import random           #Libary für zufällige Nummern(unötig)

GPIO.setwarnings(False) #Ausschalten der Warnmeldung der GPIO-Pins
GPIO.setmode(GPIO.BCM)   #Einschalten in das Breadboard-Pin system

gefundenG = False   #Gewicht gefunden Bool(True or False)
gefundenH = False   #Hindernis gefunden Bool
verlorenH = False   #Hindernis verloren Bool
gefundenZ = False   #Ziel gefunden Bool
drehenF = False     #Drehen Fertig Bool

Lenkung = 0.5  #Statische(?) Varibale für die Lenkung 1 = voll rechts, -1 = voll links
power1 = 0x6b       #Hexadezimaladresse für den Strom des gyroscope
power2 = 0x6c       #?
TrigA = 23          #Varibale TRIGGER ist GPIO-Pinnummer für das Auslösen des US-Sensors
EchoA = 24          #Varibale Echo ist die GPIO-Pinnummer für den Pin des Echos/Output des Us-Sensors
TrigB = 17          #
EchoB = 27          #
MA1_Pin = 25
MA2_Pin = 8
MB1_Pin = 7
MB2_Pin = 12
MC1_Pin = 10
MC2_Pin = 9
bus = smbus.SMBus(1)    #Starten des Datenbus-System für das Gyroscope
address = 0x68 #Hexadezimaladresse des Gyroscope 

GPIO.setup(TrigA, GPIO.OUT)    #init der Pins
GPIO.setup(EchoA, GPIO.IN)    #
GPIO.setup(TrigB, GPIO.OUT)    #init der Pins
GPIO.setup(EchoB, GPIO.IN)    #
GPIO.setup(MA1_Pin, GPIO.OUT)
GPIO.setup(MA2_Pin, GPIO.OUT)
GPIO.setup(MB1_Pin, GPIO.OUT)
GPIO.setup(MB2_Pin, GPIO.OUT)
GPIO.setup(MC1_Pin, GPIO.OUT)
GPIO.setup(MC2_Pin, GPIO.OUT)
MotorA1 = GPIO.PWM(MA1_Pin, 50)                #Pins der Motoren festlegen und Frequenz
MotorB1 = GPIO.PWM(MB1_Pin, 50)                #
MotorC1 = GPIO.PWM(MC1_Pin, 50)                #
MotorA2 = GPIO.PWM(MA2_Pin, 50)                #
MotorB2 = GPIO.PWM(MB2_Pin, 50)                 #
MotorC2 = GPIO.PWM(MC2_Pin, 50)                #

MotorA1.start(0)    #Starten der Motoren ohne Drehung
MotorA2.start(0)    #
MotorB1.start(0)    #
MotorB2.start(0)    #
MotorC1.start(0)    #
MotorC2.start(0)    #

def Vorwaerts(KraftV):  #vorwaerts waren mit der Angegeben geschwindigkeit in % der maximal Leistung
    MotorA1.ChangeDutyCycle(KraftV)
    MotorB1.ChangeDutyCycle(KraftV)
    
def Rueckwaerts(KraftR): #das gleiche für rückwärts fahren(nicht nötig)
    MotorA2.ChangeDutyCycle(KraftR)
    MotorB2.ChangeDutyCycle(KraftR)

def DrehenStelle(KraftD):# Auf der stelle drehen
    MotorA1.ChangeDutyCycle(KraftD)
    MotorB2.ChangeDutyCycle(KraftD)

def Stop(): #alle Fahr-motoren stoppen
    MotorA1.ChangeDutyCycle(0)
    MotorA2.ChangeDutyCycle(0)
    MotorB1.ChangeDutyCycle(0)
    MotorB2.ChangeDutyCycle(0)
    
def Greifen(KraftG): #greifen des gewichts
    MotorC2.ChangeDutyCycle(0)
    MotorC1.ChangeDutyCycle(KraftG)
    time.sleep(2.5)
    MotorC1.ChangeDutyCycle(0)
    MotorC1.stop()
    
def Loslassen(): #loslassen des Gewichts
    MotorC1.ChangeDutyCycle(0)
    MotorC2.ChangeDutyCycle(15)
    time.sleep(2.6)
    MotorC2.ChangeDutyCycle(0)
    MotorC2.stop()
    
def DistanzA(): #funktion der Distanzmessung des US-SensorA(voren). Gibt das Ergebnis in cm wieder
    
    GPIO.output(TrigA, GPIO.LOW) #Erholungszeit für den Sensor? (Wird eindeutig noch verändert9
    
    GPIO.output(TrigA, GPIO.HIGH) #Auslösen des US-Sensor für ein Bruchteil einer Sekunde
    time.sleep(0.00001)
    GPIO.output(TrigA, GPIO.LOW)
    
    while GPIO.input(EchoA)==0:      #zeitpunkt des Auslösen festnehemn
        PulsStartA = time.time()
        
    while GPIO.input(EchoA)==1:      #Zeitpunkt der Aufnahme des Echos
        PulsEndeA = time.time()
                     
    PulsDauerA = PulsEndeA - PulsStartA  #Ausrechnen der zeit differenz zwischen auslösen und des Echo
                     
    DistanzA = PulsDauerA * 17150        #Ausrechnen der Distanz anhand zeitdifferenz * Schallgeschwindigkeit 
    DistanzA = round(DistanzA, 2)         #runden des Ergebnis auf 2 nachkommastellen
    return DistanzA

def DistanzB(): #das gleiche für US-SensorB(Hinten)
    
    PulsStartB = time.time()
    
    GPIO.output(TrigB, GPIO.LOW) #Erholungszeit für den Sensor? (Wird eindeutig noch verändert9
    
    GPIO.output(TrigB, GPIO.HIGH) #Auslösen des US-Sensor für ein Bruchteil einer Sekunde
    time.sleep(0.00001)
    GPIO.output(TrigB, GPIO.LOW)
    
    while GPIO.input(EchoB)==0:      #zeitpunkt des Auslösen festnehemn
        PulsStartB = time.time()
        
    while GPIO.input(EchoB)==1:      #Zeitpunkt der Aufnahme des Echos
        PulsEndeB = time.time()
                     
    PulsDauerB = PulsEndeB - PulsStartB  #Ausrechnen der zeit differenz zwischen auslösen und des Echo
                     
    DistanzB = PulsDauerB * 17150        #Ausrechnen der Distanz anhand zeitdifferenz * Schallgeschwindigkeit 
    DistanzB = round(DistanzB, 2)         #runden des Ergebnis auf 2 nachkommastellen
    return DistanzB

def byteLesen(reg): #Lesen der Ausgabe des gyroscope
    return bus.read_byte_data(address, reg)
    
def wordLesen(reg): #1.schritt zum auslesen eines 16-bit word
    high = bus.read_byte_data(address, reg)

def wordLesen_2c(reg): #2.schritt zum auslesen eines 16-bit word
    wert = wordLesen(reg)
    if (wert >= 0x8000):
        return -((65535 - wert) + 1)
    else:
        return wert
        
def distanz(a,b): #Satz des phytagoras
    return math.sqrt((a*a)+(b*b))
    
def get_y_rotation(x,y,z): #Accelormeter y rotation
    radien = math.atan2(x, distanz(y,z))
    return -math.degrees(radien)
    
def get_x_rotation(x,y,z): #Accelormeter x rotation
    radien = math.atan2(y, distanz(x,z))
    return math.degrees(radien)

Vorwaerts(40)
        
time.sleep(1.5)

Stop()
print("Am gewicht")
Greifen(30) #Greifen des Gewichts
print("Gewicht gegriffen")

Vorwaerts(40) #Zum hindernis fahren
while gefundenH == False:   #Der Seitliche ultraschall-sensor schaut nach dem Hindernis und speichert die Entfernung
    if  DistanzB() < 35 and DistanzB() < 35:
        HindernisDistanz = DistanzB() + 10
        gefundenH = True

print("Hindernis gefunden")

while verlorenH == False:   #Der Seitliche US-Sensor gibt an wenn er das Hindernis nicht mehr sieht, Fahrzeug fährt 2sek weiter und stoppt 
    if DistanzB() > HindernisDistanz and DistanzB() > HindernisDistanz:
        time.sleep(2)
        Stop()
        verlorenH = True

print("Hindernis verloren")

time.sleep(1)

'''
bus.write_byte_data(address,power1,0)   #der gyroscope wird initalisiert
#TODO Gyro
GyX = wordLesen_2c(0x43) #Die ausgabe der X-Achse des Gyros wird gelsesen
StartX = GyX / 131  #(?) Wird in Grad umgerechnet

if random.randint(0,1) == 1: #Temp Spaß-Funktion Munz-Wurf zum auswählen der Dreh-Methode
    Kurve() #
else:
    DrehenStelle(30)
'''

DrehenStelle(100)

'''
while drehenF == False: #Am Gyroscope auslesen ob man sich um 90° gedreht hat
    if (StartX - wordLesen_2c(0x43)) > 90:
        Stop()
        drehenF = True
''' 
        
time.sleep(2.00)
Stop()

print("Gedreht")

Vorwaerts(40) #langsam vorwaerts

while gefundenZ == False: #wenn näher als 50cm zum schrank gewicht fallen lassen
    if DistanzA() < 50 && DistanzA() < 50:
        Stop()
        gefundenZ = True

print("Ziel gefunden")

time.sleep(2)
Loslassen() #gehört zur dem daruber

print("Gewicht losgelassen")

MotorA1.stop
MotorA2.stop  #Moteren anhalten
MotorB1.stop
MotorB2.stop
MotorC1.stop
MotorC2.stop
GPIO.cleanup                  #Gpio output und input beenden
print("Cleanup")
print("Fertig")