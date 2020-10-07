#!/usr/bin/env python

"""main.py: This project made by Hacettepe University Robotics Society for orientation days."""

__author__      = "Muhammed Baki Almaci & Ugurcan Erdogan"
__copyright__   = "Copyright HUNROBOTX 2019, Hacettepe University"

import keyboard  # Using module keyboard to catch pressed buttons from keyboard.
import time # Using sleep library.
import RPi.GPIO as GPIO # To usign Raspberry Pi pin outs.

GPIO.setmode(GPIO.BCM) # Look at here: https://raspberrypi.stackexchange.com/questions/12966/what-is-the-difference-between-board-and-bcm-for-gpio-pin-numbering
GPIO.setwarnings(False) # Escape from unexpected errors.
GPIO.cleanup() # Sometimes Raspberry Pi pins hanging their previous state. This is an unwanted case. We need to clear.

# Left motors pin
left1 = 26
left2 = 20
leftPWM = 100
# Right motors pin
right1 = 1
right2 = 2
rightPWM = 100

# There is some GPIO settings for movement.
GPIO.setup(left1, GPIO.OUT)
GPIO.setup(left2, GPIO.OUT)
GPIO.setup(right1, GPIO.OUT)
GPIO.setup(right2, GPIO.OUT)

# There is defined PWM to GPIO pins.
leftPWM  =  GPIO.PWM(leftPWM, 100)
rightPWM = GPIO.PWM(rightPWM, 100)

time.sleep(1) # Waiting 1 second for optimization.

def forward():
    GPIO.output(left1, GPIO.HIGH)
    GPIO.output(left2, GPIO.LOW)
    GPIO.output(right1, GPIO.HIGH)
    GPIO.output(right2, GPIO.LOW)
    leftPWM.start(80) # Don't forget that max value of PWM is 100. (In arduino it can be 255)
    rightPWM.start(80) # Don't forget that max value of PWM is 100. (In arduino it can be 255)

def left():
    GPIO.output(left1, GPIO.HIGH)
    GPIO.output(left2, GPIO.LOW)
    GPIO.output(right1, GPIO.HIGH)
    GPIO.output(right2, GPIO.LOW)
    leftPWM.start(30) # Don't forget that max value of PWM is 100. (In arduino it can be 255)
    rightPWM.start(80) # Don't forget that max value of PWM is 100. (In arduino it can be 255)

def right():
    GPIO.output(left1, GPIO.HIGH)
    GPIO.output(left2, GPIO.LOW)
    GPIO.output(right1, GPIO.HIGH)
    GPIO.output(right2, GPIO.LOW)
    leftPWM.start(80) # Don't forget that max value of PWM is 100. (In arduino it can be 255)
    rightPWM.start(30) # Don't forget that max value of PWM is 100. (In arduino it can be 255)

def back():
    GPIO.output(left2, GPIO.HIGH)
    GPIO.output(left1, GPIO.LOW)
    GPIO.output(right2, GPIO.HIGH)
    GPIO.output(right1, GPIO.LOW)
    leftPWM.start(80) # Don't forget that max value of PWM is 100. (In arduino it can be 255)
    rightPWM.start(80) # Don't forget that max value of PWM is 100. (In arduino it can be 255)

def handbrake():
    GPIO.output(left1, GPIO.HIGH)
    GPIO.output(left2, GPIO.HIGH)
    GPIO.output(right1, GPIO.HIGH)
    GPIO.output(right2, GPIO.HIGH)
    leftPWM.start(0) # Don't forget that max value of PWM is 100. (In arduino it can be 255)
    rightPWM.start(0) # Don't forget that max value of PWM is 100. (In arduino it can be 255)

while True: # To make infinite loop.
    try:
        if keyboard.is_pressed('w'):
            print('Go Ahead') # These prints are not necessary but they gives info to user.
            forward()
        elif keyboard.is_pressed('s'): 
            print('Turn Back') # These prints are not necessary but they gives info to user.
            back()
        elif keyboard.is_pressed('a'): 
            print('Turn Left') # These prints are not necessary but they gives info to user.
            left()
        elif keyboard.is_pressed('d'):  
            print('Turn Right') # These prints are not necessary but they gives info to user.
            right()
        elif keyboard.is_pressed(' '):  
            print('HandBrake!') # These prints are not necessary but they gives info to user.
            handbrake()
        elif keyboard.is_pressed('esc'): 
            print('Exited.') # These prints are not necessary but they gives info to user.
            GPIO.cleanup() # Sometimes Raspberry Pi pins hanging their previous state. This is an unwanted case. We need to clear.
            break
        else:
            pass # If pressed unexpected key, don't care it.
    except:
        GPIO.cleanup() # Sometimes Raspberry Pi pins hanging their previous state. This is an unwanted case. We need to clear.
        break  # If there is unexpected event, shut down!.