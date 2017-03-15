#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time


class MotionSensorPeriodic(object):
    def __init__(self):
      self.channel = 17

    def detect(self, sender, earg):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.channel, GPIO.IN)

        while True:
            try:
                print('検知中')
                if GPIO.input(self.channel):
                    print('検知しました')
                    self.user_method2()

                self.user_method1()
                time.sleep(1)
            except:
                self.exception_method()

    def user_method1(self, earg=None):
        print('call user method')

    def user_method2(self, earg=None):
        print('hello, world')

    def exception_method(self):
        GPIO.cleanup(self.channel)

t = MotionSensorPeriodic()
t.detect(1,2)
