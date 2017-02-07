#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
from demand_gpio_sensor import DemandGpicGpioSensor
from demand import Demand

class SonicSensorPeriodci(PeriodicGpioSensor):
    def __init__(self):
        self.demand = Demand(mode='double', event=1, pulse_time=0.0001)
        super().__init__([21, 20])
        self.user_methods = [sensor_method, user_method1]
        self.event_handler.add_event_handler(20, user_method2)
        self.pulse_start = 0
        self.pulse_end = 0
        self.pulse_duration = 0
        self.distance = 0

    def main(self):
        print("Distance Measurement in Progress")
        super().demand_issue(self.demand, start_method, 'high', 0.0001)
        self.demand.set_mode(None)
        super().demand_issue(self.demand, sensor_method, 'low', 0.0001)

    def start_method(self):
        self.loop_flag = 0
        self.pulse_start = time.time()

    def sensor_method(self):
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
            pass

    def user_method1(self, earg=None):
        print('call user method')

    def user_method2(self, earg=None):
        print('hello, world')
