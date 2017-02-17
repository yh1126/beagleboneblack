#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time


class MotionSensorEvent(object):
    def __init__(self):
        self.channel = 17

    def detect(self, sender, earg):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.channel, GPIO.IN)
        GPIO.add_event_detect(self.channel, GPIO.RISING)
        GPIO.add_event_callback(self.channel, self.user_method1)
        GPIO.add_event_callback(self.channel, self.user_method2)

        while True:
            try:
                print('検知中')
                time.sleep(0.1)
            except:
                self.exception_method()
  
    def user_method1(self, *x):
        print('call user method')
  
    def user_method2(self, *x):
        print('hello, world')

    def exception_method(self):
        GPIO.cleanup(self.channel)
        GPIO.remove_event_detect(self.channel)

t = MotionSensorEvent()
t.detect(1,2)
