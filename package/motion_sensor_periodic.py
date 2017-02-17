#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
from periodic_gpio_sensor import PeriodicGpioSensor


class MotionSensorPeriodic(PeriodicGpioSensor):
    def __init__(self):
        super().__init__(17, 1)
        self.user_methods = [self.user_method, self.user_method1]
        self.event_handler.add_event_handler(1, self.user_method2)

    def main(self):
        #super().periodic_read(self.user_methods)
        super().periodic_read(self.user_method)
        while True:
            print('別スレッド')
            time.sleep(1)

    def user_method(self):
        self.sensor_value = GPIO.input(self.channel[0])
        print(self.sensor_value)
        print('検知中')


    def user_method1(self, channel):
        print('call user method')

    def user_method2(self, channel):
        print('hello, world')

t = MotionSensorPeriodic()
#t.user_method()
t.main()
