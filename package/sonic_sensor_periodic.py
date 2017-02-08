#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
from periodic_gpio_sensor import PeriodicGpioSensor


class SonicSensorPeriodic(PeriodicGpioSensor):
    def __init__(self):
        super().__init__([20, 21], 2)
        self.user_methods = [self.sensor_method, self.user_method1]
        self.event_handler.add_event_handler(20, self.user_method2)
        self.pulse_start = 0
        self.pulse_end = 0
        self.pulse_duration = 0
        self.distance = 0

    def main(self):
        self.periodic_read(self.user_methods)

    def sensor_method(self):
        print("Distance Measurement in Progress")
        GPIO.setup(self.channel[0], GPIO.IN)
        GPIO.setup(self.channel[1], GPIO.OUT)
        GPIO.output(self.channel[1], GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self.channel[1], GPIO.LOW)

        while GPIO.input(self.channel[0]) == 0:
            self.pulse_start = time.time()

        while GPIO.input(self.channel[0]) == 1:
            self.pulse_end = time.time()

        self.pulse_duration = self.pulse_end - self.pulse_start
        self.distance = self.pulse_duration * 17150
        self.distance = round(self.distance, 2)
        print("Distance: ", self.distance, "cm")
        if(self.distance < 20):
            self.sensor_value = 20
        else:
            self.sensor_value = None

    def user_method1(self, earg=None):
        print('call user method')

    def user_method2(self, earg=None):
        print('hello, world')
