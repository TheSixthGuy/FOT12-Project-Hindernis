#!/Phyton/Sensoren-Funktion.py
#https://electrosome.com/hc-sr04-ultrasonic-sensor-raspberry-pi/

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIGGER = 23
ECHO = 24

GPIO.setup(TRIGGER,GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

while True:
    
    GPIO.output(TRIGGER, GPIO.LOW)
    print ("Warten...")
    time.sleep(2)
    
    GPIO.output(TRIGGER, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIGGER, GPIO.LOW)
    
    while GPIO.input(ECHO)==0:
        Puls_Start = time.time()
        
    while GPIO.input(ECHO)==1:
        Puls_Ender = time.time()
                     
    Puls_Dauer = Puls_Ende - Puls-Start
                     
    Distanz = Puls_Dauer * 17150
    Distanz = round(Distanz, 2)
    
    if Distanz > 2 and Distanz < 400:
        print ("Gefunden!")
        #Motor Stop
        #Grip()
    else:
        print ("Suchen...")
    
GPIO.cleanup

#Bis KW13