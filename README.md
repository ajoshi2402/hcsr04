# HCSR04-raspberrypi
The module is a sensor which can measure distance and runs with 5V, so be aware of the Echo pin, it needs a voltage devider to have a lower voltage then 3.3V.

Here is a reference sheet for the module: www.micropik.com/PDF/HCSR04.pdf

I used the GPIO.BOARD mode and for the trigger(output) pin 11 and for echo(input) the pin 13, it can be changed to what ever you want.

Please see the test file for further explanation.
