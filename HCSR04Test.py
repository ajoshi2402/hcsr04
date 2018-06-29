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

GPIO.setwarnings(False)

try:
    while True:
        print("Distance: %.2fcm" %(hcsr.distance(-0.5))) # Offset to -0.5 | Round to the second decimal
        time.sleep(10)

except KeyboardInterrupt:
    GPIO.cleanup()
