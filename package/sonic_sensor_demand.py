#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
from demand_gpio_sensor import DemandGpioSensor
from demand import Demand

class SonicSensorDemand(DemandGpioSensor):
    def __init__(self):
        self.demand = Demand(mode='double', edge=1, pulse_time=0.00001)
        super().__init__([20, 21])
        self.user_methods = [self.sensor_method, self.user_method1]
        self.event_handler.add_event_handler(20, self.user_method2)
        self.pulse_start = 0
        self.pulse_end = 0
        self.pulse_duration = 0
        self.distance = 0

    def main(self):
        print("Distance Measurement in Progress")
        super().demand_issue(self.demand, self.start_method, 'high')
        self.demand.set_mode(None)
        super().demand_issue(self.demand, self.sensor_method, 'low')

    def start_method(self, earg=None):
        self.loop_flag = 0
        self.pulse_start = time.time()

    def sensor_method(self, earg=None):
        self.loop_flag = 0
        self.pulse_end = time.time()
        self.pulse_duration = self.pulse_end - self.pulse_start
        self.distance = self.pulse_duration * 17150
        self.distance = round(self.distance, 2)
        print("Distance: ", self.distance, "cm")
        if(self.distance < 20):
            self.sensor_value = 20
            if self.sensor_value in self.event_handler:
                self.event_handler()
        else:
            self.sensor_value = None

    def user_method1(self, earg=None):
        print('call user method')

    def user_method2(self, earg=None):
        print('hello, world')
