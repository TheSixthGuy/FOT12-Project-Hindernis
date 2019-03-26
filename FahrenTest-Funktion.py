#!/pi/dokumente/Phyton/Fahren-Funktion.py

import RPi.GPIO as GPIO  #Zum ansprechen der Pins
import time              #Zum einsetzen von Zeit-basierte Funktionen

GPIO.setwarnings(False)  #Zum ausschalten von nicht kritischen fehlermeldungen

GPIO.setmode(GPIO.BCM)   #Einschalten des Boardmode(Pin-nummerierung)
print("Boardmode set")

MotorA = 25                #GPIO-PIN-Nummer der Motoren in deren variable speichern
MotorB = 7 
MotorC = 10

MotorA_pwm = 8
MotorB_pwm = 12
MotorC_pwm = 9

GPIO.setup(MotorA, GPIO.OUT)  #Pins als Ausgange definieren
GPIO.setup(MotorB, GPIO.OUT)  #
GPIO.setup(MotorC, GPIO.OUT)
GPIO.setup(MotorA_pwm, GPIO.OUT)
GPIO.setup(MotorB_pwm, GPIO.OUT)
GPIO.setup(MotorC_pwm, GPIO.OUT)

#pwmA = GPIO.PWM()


GPIO.cleanup                  #
print("Cleanup")

'''
def SetAngleA(angle):         #Funktion um die gewollte Drehung der Motoren auszuführen
    duty = angle / 18 + 2          #Benötiger Arbeitszyklus ausrechnen
    GPIO.output(MotorA, GPIO.HIGH)  #Ausgabe auf den PIN von MotorA
    pwm.ChangeDutyCycle(duty)       #Ändern des Arbeitszyklus auf den ausgerechneten Wert
    time.sleep(1)                   #1 Sekunde warten
    GPIO.output(MotorA,GPIO.LOW)    #Ausgabe auf den PIN von MotorA beenden
    pwm.ChangeDutyCycle(0)          #Ändern des Arbeitszyklus auf 0

def SetAngleB(angle):         #Kopie von SetAngleA aber für MotorB
    duty = angle / 18 + 2
    GPIO.output(MotorB, GPIO.HIGH)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(MotorB,GPIO.LOW)
    pwm.ChangeDutyCycle(0)    
'''
'''
pwmA=GPIO.PWM(MotorA, 50)     #Pulse Width Modulation einstellen. Nötig für Servomotoren
pwmB=GPIO.PWM(MotorB, 50)     #

pwmA.start(0)                 #Arbeitszyklus auf 0 setzen damit keine Drehung gesetzt wird
pwmB.start(0)                 #

SetAngleA(90)                 #Um 90 Grad nach vorne Drehen (ungestestet)
SetAngleB(90)                 #

pwm.stop()                    #Beenden der Motor Steuerung
'''
