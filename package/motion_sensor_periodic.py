#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
from periodic_gpio_sensor import PeriodicGpioSensor


class MotionSensorPeriodic(PeriodicGpioSensor):
    def __init__(self):
        super().__init__(18, 0.1)
        self.user_method = [sensor_method, user_method1]
        super().event_handler.add_event_handler(1, user_method2)

    def main(self):
        super().periodic_read(self, user_method)

    def sensor_method(self):
        self.sensor_value = GPIO.input(self.channel[0])
        print('検知中')

    def user_method1(self, None):
        print('call user method')

    def user_method2(self, None):
        print('hello, world')
