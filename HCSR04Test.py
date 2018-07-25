#!/usr/bin/python3
# coding=utf-8
#-----------------------------------------
# HC-SR04 Ultrasonic Ranging Module Test
#-----------------------------------------
#
# Use this script as an example.


import RPi.GPIO as GPIO
import HCSR04Ultrasonic as hcsr
import time
from time import sleep
import urllib
from bs4 import BeautifulSoup

GPIO.setwarnings(False)

try:
    while True:
        print("Distance: %.2fcm" %(hcsr.distance(-0.5))) # Offset to -0.5 | Round to the second decimal
        data=urllib.urlopen("https://api.thingspeak.com/update?api_key=NVBW0ZTQ2W3BNTK2&field1="+str(hcsr);
        print data
	data.read()
	data.close()
	time.sleep(5)

except KeyboardInterrupt:
    GPIO.cleanup()
