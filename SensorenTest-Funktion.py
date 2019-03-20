#!/Phyton/Sensoren-Funktion.py
#https://electrosome.com/hc-sr04-ultrasonic-sensor-raspberry-pi/

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIGGER = 23                    #Varibale TRIGGER ist GPIO-Pinnummer für das Auslösen des US-Sensors
ECHO = 24                       #Echo ist die ausgabe des sensors

GPIO.setup(TRIGGER,GPIO.OUT)    #init der Pins
GPIO.setup(ECHO, GPIO.IN)

while True:
    
    GPIO.output(TRIGGER, GPIO.LOW) #Erholungszeit für den Sensor? (Wird eindeutig noch verändert9
    print ("Warten...")
    time.sleep(2)
    
    GPIO.output(TRIGGER, GPIO.HIGH) #Auslösen des US-Sensor für ein Bruchteil einer Sekunde
    time.sleep(0.00001)
    GPIO.output(TRIGGER, GPIO.LOW)
    
    while GPIO.input(ECHO)==0:      #zeitpunkt des Auslösen festnehemn
        Puls_Start = time.time()
        
    while GPIO.input(ECHO)==1:      #Zeitpunkt der Aufnahme des Echos
        Puls_Ende = time.time()
                     
    Puls_Dauer = Puls_Ende - Puls-Start  #Ausrechnen der zeit differenz zwischen auslösen und des Echo
                     
    Distanz = Puls_Dauer * 17150        #Ausrechnen der Distanz anhand zeitdifferenz * Schallgeschwindigkeit 
    Distanz = round(Distanz, 2)         #runden des Ergebnis auf 2 nachkommastellen
    
    if Distanz > 2 and Distanz < 400:   # bei näher als 2 cm ist gewicht gefunden 
        print ("Gefunden!")
        #Motor Stop
        #Grip()
    else:
        print ("Suchen...")             # bei weiter weg als 2 cm ist noch am suche dann von vorne anfangen
    
GPIO.cleanup

#Bis KW13
