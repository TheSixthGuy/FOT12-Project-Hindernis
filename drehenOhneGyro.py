#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO #Libary für die Benutzung von den GPIO-Pins
import time             #Libary für Zeit-basierte Funktionen

GPIO.setwarnings(False) #Ausschalten der Warnmeldung der GPIO-Pins
GPIO.setmode(GPIO.BCM)   #Einschalten in das Breadboard-Pin system

MA1_Pin = 25
MA2_Pin = 8
MB1_Pin = 7
MB2_Pin = 12

GPIO.setup(MA1_Pin, GPIO.OUT)
GPIO.setup(MA2_Pin, GPIO.OUT)
GPIO.setup(MB1_Pin, GPIO.OUT)
GPIO.setup(MB2_Pin, GPIO.OUT)
MotorA1 = GPIO.PWM(MA1_Pin, 50)                #Pins der Motoren festlegen und Frequenz
MotorB1 = GPIO.PWM(MB1_Pin, 50)                #
MotorA2 = GPIO.PWM(MA2_Pin, 50)                #
MotorB2 = GPIO.PWM(MB2_Pin,50)                 #


MotorA1.start(0)    #Starten der Motoren ohne Drehung
MotorA2.start(0)    #
MotorB1.start(0)    #
MotorB2.start(0)    #

def DrehenStelle(KraftD):# Auf der stelle drehen
    MotorA1.ChangeDutyCycle(KraftD)
    MotorB2.ChangeDutyCycle(KraftD)

def Stop(): #alle Fahr-motoren stoppen
    MotorA1.ChangeDutyCycle(0)
    MotorA2.ChangeDutyCycle(0)
    MotorB1.ChangeDutyCycle(0)
    MotorB2.ChangeDutyCycle(0)

DrehenStelle(100)
time.sleep(2.65)
Stop()

MotorA1.stop
MotorA2.stop  #Moteren anhalten
MotorB1.stop
MotorB2.stop
GPIO.cleanup                  #Gpio output und input beenden
print("Cleanup")
print("Fertig")