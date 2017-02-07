#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time


class MotionSensorEvent(object):

  def __init__(self):
      self.channel = 18

  def detect(self, sender, earg):
      GPIO.setmode(GPIO.BCM)
      GPIO.setup(self.channel, GPIO.IN)
      GPIO.add_event_detect(self.channel, GPIO.RIGING)
      GPIO.add_event_callback(self.channel, user_method1)
      GPIO.add_event_callback(self.channel, user_method2)

    while True:
        try:
            print('検知中')
            time.sleep(0.1)
        except:
            self.exception_method()

        def user_method1(self):
            print('call user method')

        def user_method2(self):
            print('hello, world')

        def exception_method(self):
            GPIO.cleanup(self.channel)
            GPIO.remove_event_detect(self.channel)
