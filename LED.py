#2025-3-31
#made by Guo

import RPi.GPIO as GPIO
import time# Imports the Time library so that we can pause the script later on.
GPIO.setmode(GPIO.BCM)# Each pin on the Raspberry Pi has several different names, so you need to tell the 
program which naming convention is to be used.
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
print("LED on")# This line prints some information to the terminal
GPIO.output(18,GPIO.HIGH)#This turns the GPIO pin ‘on’. What this actually means is that the pin is made to 
provide power of 3.3volts. This is enough to turn the LED in our circuit on
time.sleep(1)# Pauses the Python program for 1 second
print("LED off")#This line prints some information to the terminal
GPIO.output(18,GPIO.LOW)#This turns the GPIO pin ‘off’, meaning that the pin is no longer supplying any power.
 And that's it! You are now able to turn an LED on and off
