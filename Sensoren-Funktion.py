#!/Phyton/Sensoren-Funktion.py
#https://electrosome.com/hc-sr04-ultrasonic-sensor-raspberry-pi/

import RPI.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIGGER = 23
ECHO = 24

while True:
    
    GPIO.output(TRIGGER, GPIO.LOW)
    