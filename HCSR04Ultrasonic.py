#/usr/bin/python3
#------------------------------------
# HC-SR04 Ultrasonic Ranging Module
# -----------------------------------
#
# For use with Raspberry Pi.
#
# Be aware of the Input from Echo,
# you need to use a voltage divider
# to reduce the voltage to under 3.3V.
#
# The trigger needs to be at least 0.00001 seconds high.
#
# distance = (time * velocity of sound) / 2
#

import RPi.GPIO as GPIO
import time

# If you use BCM, change here and the following pins accordingly.
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Set these pins to your current wiring.
trig = 11
echo = 13

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

# If you know define offset.
def distance(offset = 0):
    GPIO.output(trig, GPIO.LOW)

    time.sleep(2) # Give the sensor some time, can be adjusted, without gives sometimes bad values.
    
    GPIO.output(trig, GPIO.HIGH)
    time.sleep(0.00001) # Only for 0.00001 seconds.
    GPIO.output(trig, GPIO.LOW)

    while GPIO.input(echo) == GPIO.LOW:
        pass

    startTime = time.time()

    while GPIO.input(echo) == GPIO.HIGH:
        pass

    endTime = time.time()

    distance = ((endTime - startTime) * 34300) / 2 # distance in cm, change the velocity of sound to use for other sizes.

    return distance + offset
   
