#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO #Libary für die Benutzung von den GPIO-Pins
import time             #Libary für Zeit-basierte Funktionen

GPIO.setwarnings(False) #Ausschalten der Warnmeldung der GPIO-Pins
GPIO.setmode(GPIO.BCM)  #Nummerierung nach BCM(GPIO-PIN haben feste Nummern)

TrigA = 23          #Varibale TRIGGER ist gleich GPIO-Pinnummer für das Auslösen des US-Sensors
EchoA = 24          #Varibale Echo ist gleich die GPIO-Pinnummer für den Pin des Echos/Output des US-Sensors
TrigB = 17          #
EchoB = 27          #
MA1_Pin = 25        #Variable fuer Motor A Pin 1
MA2_Pin = 8         #Variable fuer Motor A Pin 2
MB1_Pin = 7         #Variable fuer Motor B Pin 1
MB2_Pin = 12        #Variable fuer Motor B Pin 2
MC1_Pin = 10        #Variable fuer Motor C Pin 1
MC2_Pin = 9         #Variable fuer Motor C Pin 2

GPIO.setup(TrigA, GPIO.OUT)     #init der Pins fuer US-Sensor als Ausgang
GPIO.setup(EchoA, GPIO.IN)      #               "             als Eingang
GPIO.setup(TrigB, GPIO.OUT)     #
GPIO.setup(EchoB, GPIO.IN)      #
GPIO.setup(MA1_Pin, GPIO.OUT)   #init der Pins fuer Motoren
GPIO.setup(MA2_Pin, GPIO.OUT)   #
GPIO.setup(MB1_Pin, GPIO.OUT)   #
GPIO.setup(MB2_Pin, GPIO.OUT)   #
GPIO.setup(MC1_Pin, GPIO.OUT)   #
GPIO.setup(MC2_Pin, GPIO.OUT)   #
MotorA1 = GPIO.PWM(MA1_Pin, 50)                #Pins der Motoren auf PWM(Pulse Width Modulation) einstellen mit 50Hz
MotorB1 = GPIO.PWM(MB1_Pin, 50)                #
MotorC1 = GPIO.PWM(MC1_Pin, 50)                #
MotorA2 = GPIO.PWM(MA2_Pin, 50)                #
MotorB2 = GPIO.PWM(MB2_Pin, 50)                #
MotorC2 = GPIO.PWM(MC2_Pin, 50)                #

MotorA1.start(0)    #Starten der Motoren ohne Drehung
MotorA2.start(0)    #
MotorB1.start(0)    #
MotorB2.start(0)    #
MotorC1.start(0)    #
MotorC2.start(0)    #

def Vorwaerts(KraftV):  #vorwaerts fahren mit der Angegeben geschwindigkeit in % der maximal Leistung
    MotorA1.ChangeDutyCycle(KraftV)
    MotorB1.ChangeDutyCycle(KraftV)

def DrehenStelle(KraftD):# Auf der stelle drehen
    MotorA1.ChangeDutyCycle(KraftD)
    MotorB2.ChangeDutyCycle(KraftD)

def Stop(): #alle Reifenmotoren stoppen
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
    
def DistanzA(): #funktion der Distanzmessung des US-SensorA(vorne). Gibt das Ergebnis in cm wieder
    
    GPIO.output(TrigA, GPIO.LOW) #Redundanz für niedrigere Fehlerquote
    
    GPIO.output(TrigA, GPIO.HIGH) #Auslösen des US-Sensor für ein Bruchteil einer Sekunde
    time.sleep(0.00001)           #0,00001 sek warten
    GPIO.output(TrigA, GPIO.LOW)  #
    
    while GPIO.input(EchoA)==0:      #zeitpunkt des Auslösen festnehemn
        PulsStartA = time.time()
        
    while GPIO.input(EchoA)==1:      #Zeitpunkt der Aufnahme des Echos festnehem
        PulsEndeA = time.time()
                     
    PulsDauerA = PulsEndeA - PulsStartA  #Ausrechnen der zeit differenz zwischen dem auslösen und des Echo
                     
    DistanzA = PulsDauerA * 17150        #Ausrechnen der Distanz anhand zeitdifferenz * Schallgeschwindigkeit in der Luft in cm/s²
    DistanzA = round(DistanzA, 2)        #runden des Ergebnis auf 2 nachkommastellen
    return DistanzA                      #Rückgabe des Wertes

def DistanzB(): #das gleiche für US-SensorB(Hinten)
    
    GPIO.output(TrigB, GPIO.LOW) #Redundanz für niedrigere Fehlerquote
    
    GPIO.output(TrigB, GPIO.HIGH) #Auslösen des US-Sensor für ein Bruchteil einer Sekunde
    time.sleep(0.00001)           #0,00001 sek warten
    GPIO.output(TrigB, GPIO.LOW)  #
    
    while GPIO.input(EchoB)==0:      #Zeitpunkt des Auslösen festnehmen
        PulsStartB = time.time()
        
    while GPIO.input(EchoB)==1:      #Zeitpunkt der Aufnahme des Echos festnehmen
        PulsEndeB = time.time()
                     
    PulsDauerB = PulsEndeB - PulsStartB  #Ausrechnen der Zeitdifferenz zwischen dem auslösen und des Echo
                     
    DistanzB = PulsDauerB * 17150        #Ausrechnen der Distanz anhand zeitdifferenz * Schallgeschwindigkeit in der Luft in cm/s²
    DistanzB = round(DistanzB, 2)        #runden des Ergebnis auf 2 nachkommastellen
    return DistanzB                      #Rückgabe des Ergebnis

Vorwaerts(40)                            #Am Anfang für 1,5 Sekunden mit 40% Kraft nach vorne fahren, damit das Gewicht gefangen wird 
time.sleep(1.5)                          #1,5 sek warten
Stop()                                   #Stehenbleiben
print("Am gewicht")                      #

Greifen(30)                              #Greifen des Gewichts        
print("Gewicht gegriffen")               #

Vorwaerts(40)                                #Am Hindernis geradeaus vorbeifahren
while 1:                                     #Der Seitliche ultraschall-sensor schaut nach dem Hindernis und speichert die Entfernung
    if  DistanzB() < 35 and DistanzB() < 35: #Falls die Distanz zur Seite kleiner als 35cm ist, dann die Distanz speichern
        HindernisDistanz = DistanzB() + 10   #(Doppelte Distanzabfrage für niedriegere Fehlerqoute)
        break
        
print("Hindernis gefunden")

while 1:   #Der Seitliche US-Sensor gibt an wenn er das Hindernis nicht mehr sieht, Fahrzeug fährt 2sek weiter und stoppt 
    if DistanzB() > HindernisDistanz and DistanzB() > HindernisDistanz: #Distanz nach rechts muss größer sein als die gespeicherte Distanz zum Hindernis
        time.sleep(2) #2sek warten
        Stop()
        break
        
print("Hindernis verloren")

time.sleep(1) #1sek warten

DrehenStelle(100) #mit 100% Kraft für 2.x warten (Variable abhänig von Reale Kraft der Reifen)
time.sleep(2.00)
Stop()
print("Gedreht")

Vorwaerts(40) #langsam vorwaerts mit 40% Kraft fahren

while 1:                   #wenn näher als 50cm zur Wand hinterdem Ziel gewicht fallen lassen
    if DistanzA() < 50 and DistanzA() < 50:
        Stop()
        break

print("Ziel gefunden")

time.sleep(0.5) #0,5 sek warten
Loslassen() #Gewicht loslassen

print("Gewicht losgelassen")

MotorA1.stop    #Alle Motoren anhalten
MotorA2.stop    #
MotorB1.stop    #
MotorB2.stop    #
MotorC1.stop    #
MotorC2.stop    #
GPIO.cleanup    #GPIO-Pin setups zurückstellen auf default
print("Cleanup")
print("Fertig")
