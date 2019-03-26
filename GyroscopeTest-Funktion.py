#http://www.netzmafia.de/skripten/hardware/RasPi/RasPi_I2C.html
import smbus
import math
import time

power1 = 0x6b
power2 = 0x6c

def byteLesen(reg):
	return bus.read_byte_data(address, reg)
	
def wortLesen(reg):
	high = bus.read_byte_data(address, reg)

def wortLesen_2c(reg):
	wert = wortLesen(reg)
	if (wert >= 0x8000):
		return -((65535 - wert) + 1)
	else:
		return wert
		
def distanz(a,b):
	return math.sqrt((a*a)+(b*b))
	
def get_y_rotation(x,y,z):
	radien = math.atan2(x, distanz(y,z))
	return -math.degrees(radien)
	
def get_x_rotation(x,y,z):
	radien = math.atan2(y, distanz(x,z))
	return math.degrees(radien)
	
bus = smbus.SMBus(1)
address = 0x68

bus.write_byte_data(address,power1,0)

gyroskop_xAusgabe = wortLesen_2c(0x43)
gyroskop_yAusgabe = wortLesen_2c(0x45)
gyroskop_zAusgabe = wortLesen_2c(0x47)

print ,"X Ausgabe: ", ("%5d" % gyroskop_xAusgabe), "skaliert: ", (gyroskop_xAusgabe / 131)
print ,"Y Ausgabe: ", ("%5d" % gyroskop_yAusgabe), "skaliert: ", (gyroskop_yAusgabe / 131)
print ,"Z Ausgabe: ", ("%5d" % gyroskop_zAusgabe), "skaliert: ", (gyroskop_zAusgabe / 131)