#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO #Libary für die Benutzung von den GPIO-Pins
import time             #Libary für Zeit-basierte Funktionen
import smbus            #Libary für die benutzung des Datenbus-System I2C für das gyroscope
import math             #Libary für Mathe Funktion wie z.B Wurzel von
import random           #Libary für zufällige Nummern(unötig)

GPIO.setwarnings(False) #Ausschalten der Warnmeldung der GPIO-Pins
GPIO.setmode(GPIO.BCM)   #Einschalten in das Breadboard-Pin system

TrigA = 23          #Varibale TRIGGER ist GPIO-Pinnummer für das Auslösen des US-Sensors
EchoA = 24          #Varibale Echo ist die GPIO-Pinnummer für den Pin des Echos/Output des Us-Sensors
TrigB = 17          #
EchoB = 27          #

GPIO.setup(TrigA,GPIO.OUT)    #init der Pins
GPIO.setup(EchoA, GPIO.IN)    #
GPIO.setup(TrigB,GPIO.OUT)    #init der Pins
GPIO.setup(EchoB, GPIO.IN)    #
    
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

a = True

while a == True:
    print("Vorne : ")
    print(DistanzA())
    print("Seite : ")
    print(DistanzB())
    time.sleep(0.5)
    
print("fertig")