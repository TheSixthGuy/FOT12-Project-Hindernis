#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO #Libary für die Benutzung von den GPIO-Pins
import time             #Libary für Zeit-basierte Funktionen

GPIO.setwarnings(False) #Ausschalten der Warnmeldung der GPIO-Pins
GPIO.setmode(GPIO.BCM)   #Einschalten in das Breadboard-Pin system

MC1_Pin = 10
MC2_Pin = 9

GPIO.setup(MC1_Pin, GPIO.OUT)
GPIO.setup(MC2_Pin, GPIO.OUT)
MotorC1 = GPIO.PWM(MC1_Pin, 50)                #
MotorC2 = GPIO.PWM(MC2_Pin, 50)                #

MotorC1.start(0)    #
MotorC2.start(0)    #

x = True
    
def Greifen(KraftG): #greifen des gewichts
    MotorC2.ChangeDutyCycle(0)
    MotorC1.ChangeDutyCycle(KraftG)
    time.sleep(2.5)
    MotorC1.ChangeDutyCycle(0)
    MotorC1.stop()
    
def Loslassen(): #loslassen des Gewichts
    MotorC1.ChangeDutyCycle(0)
    MotorC2.ChangeDutyCycle(20)
    time.sleep(0.5)
    MotorC2.ChangeDutyCycle(0)
    MotorC2.stop()

while x == True:
    Loslassen()
    print("1")
    time.sleep(2)
    print("2")

MotorC1.stop
MotorC2.stop
GPIO.cleanup                  #Gpio output und input beenden
print("Cleanup")
print("Fertig")