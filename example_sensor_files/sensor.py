#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import smbus
import spidev
import time
import event
import datetime
import threading


class Sensor(object):
    # this class is abstract sensor class

    def __init__(self):
    # construcutor
        self.GPIO_SWITCH = 22 # switch
        self.GPIO_LED    = 23 # led
        self.i2c = smbus.SMBus(1)
        self.address # set address
        self.spi = spidev.SpiDev()
        self.spi.open(0, 0)
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(GPIO_LED, GPIO.OUT)
        GPIO.output(GPIO_LED, GPIO.LOW)
        
    def get_sensor_value(self): # abstract method
    # describe sensor code
        try:
            time.sleep(0.5)
            return

        except KeyboardInterrupt:
            exception_method()

    def readADC(self): # abstract method
    # read ADC value 


    def my_callback(self): # abstract method
    # this method is event handler
        time.sleep(0.05) # チャタリング対策 今回はボタンを想定
        print("called callback function")

    def set_event_handler(self): # skeleton
    # add event handler to sensor
        GPIO.add_event_detect(GPIO_SWITCH, GPIO.FALING) # detect negative edge
        GPIO.add_event_callback(GPIO_SEITCH, my_callback) # call my_callback(event handler)

    def exeception_method(self): # abstract method
    # describe excception method
        print("Keyboard Interrupt, called exception method")
        GPIO.remove_event_detect(GPIO_SWITCH)
        GPIO.remove_event_detect(GPIO_LED)
        GPIO.cleanup(GPIO_SWITCH)
        GPIO.cleanup(GPIO_LED)



