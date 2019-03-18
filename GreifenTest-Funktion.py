#Greifen-Funktion
 import RPi.GPIO as GPIO
 import time
 
GPIO.setwarnings(False)  #Zum ausschalten von nicht kritischen fehlermeldungen

GPIO.setmode(GPIO.BCM)   #Einschalten des Boardmode(Pin-nummerierung)
print("Boardmode set")

MotorC = 5

GPIO.setup(MotorC, GPIO.OUT)  #Pins als Ausgange definieren
#GPIO.setup(MotorB, GPIO.OUT)  #

pwmC=GPIO.PWM(MotorA, 50)     #Pulse Width Modulation einstellen. Nötig für Servomotoren

pwmC.start(0)                 #Arbeitszyklus auf 0 setzen damit keine Drehung gesetzt wird

Grip()
time.sleep(10)

Release()
time.sleep(5)

pwm.stop()
GPIO.cleanup

def Grip():         #Funktion um die gewollte Drehung der Motoren auszuführen
    duty = 90 / 18 + 2          #Benötiger Arbeitszyklus ausrechnen
    GPIO.output(MotorC, GPIO.HIGH)  #Ausgabe auf den PIN von MotorA
    pwm.ChangeDutyCycle(duty)       #Ändern des Arbeitszyklus auf den ausgerechneten Wert
    #time.sleep(1)                   #1 Sekunde warten
   
	
def Release():
	GPIO.output(MotorC,GPIO.LOW)    #Ausgabe auf den PIN von MotorA beenden
	pwm.ChangeDutyCycle(0)
	duty = -90 / 18 + 2
	GPIO.output(MotorC, GPIO.HIGH)
	pwm.ChangeDutyCycle(duty)       #Ändern des Arbeitszyklus auf den ausgerechneten Wert
	time.sleep(1)
	GPIO.output(MotorC, GPIO.LOW)
	pwm.ChangeDutyCycle(0)
