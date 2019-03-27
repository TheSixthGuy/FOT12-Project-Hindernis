#!/pi/dokumente/Phyton/Fahren-Funktion.py

import RPi.GPIO as GPIO  #Zum ansprechen der Pins
import time              #Zum einsetzen von Zeit-basierte Funktionen

GPIO.setwarnings(False)  #Zum ausschalten von nicht kritischen fehlermeldungen

GPIO.setmode(GPIO.BCM)   #Einschalten des Boardmode(Pin-nummerierung)
print("Boardmode set")

MotorA1 = GPIO.PWM(25, 50)                #GPIO-PIN-Nummer der Motoren in deren variable speichern
MotorB1 = GPIO.PWM(7, 50) 
MotorC1 = GPIO.PWM(10, 50)
MotorA2 = GPIO.PWM(8, 50)
MotorB2 = GPIO.PWM(12,50)
MotorC2 = GPIO.PWM(9, 50)


GPIO.cleanup                  #
print("Cleanup")

def Greifen():
    MotorC2.ChangeDutyCycle(0)
    MotorC1.start(30)
    time.sleep(2)
    
def Loslassen():
    MotorC1.ChangeDutyCycle(0)
    MotorC2.start(30)
    time.sleep(2)
    MotorC2.ChangeDutyCycle(0)
    
def MotorTestA():
    MotorA1.start(60)
    time.sleep(1)
    MotorA1.ChangeDutyCycle(0)
    time.sleep(1)
    MotorA2.start(60)
    time.sleep(1)
    MotorA2.ChangeDutyCycle(0)
    
