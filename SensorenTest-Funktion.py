#!/Phyton/Sensoren-Funktion.py
#https://electrosome.com/hc-sr04-ultrasonic-sensor-raspberry-pi/

import RPI.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24

GPIO.setup(TRIGGER,GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

while True:
    
    GPIO.output(TRIGGER, GPIO.LOW)
    print "Warten..."
	time.sleep(2)
	
	GPIO.output(TRIG, GPIO.HIGH)
	time.sleep(0.00001)
