#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from abc import ABCMeta
import time
import types
import RPi.GPIO as GPIO
from gpio_sensor_conf import GpioSensorConf
from demand_driven_io import DemandDrivenIo
from sensor_exception import SensorException
from event_handler import EventHandler
from demand import Demand


class DemandGpioSensor(GpioSensorConf, DemandDrivenIo, SensorException):
    """This class is for the demand driven sensors"""

    def __init__(self, channel, pin_mode='BCM'):
        super().__init__(channel, pin_mode)
        self.event_handler = EventHandler()

    def demand_issue(self, demand, handlers, catch_event=None):
        self.loop_flag = 1
        if isinstance(demand, Demand):
            self.demand = demand
        else:
            print('Please give a Demand object.')
            return False

        #if catch_event.upper() == 'HIGH':
        #    GPIO.add_event_detect(self.channel[0], GPIO.RISING)
        #elif catch_event.upper() == 'LOW':
        #    GPIO.add_event_detect(self.channel[0], GPIO.FALLING)
        #elif catch_event.upper() == 'BOTH':
        #    GPIO.add_event_detect(self.channel[0], GPIO.BOTH)
        #else:
        #    return GPIO.input(self.channle[0])

 
        if isinstance(handlers, list):
            for handler in handlers:
                # if isinstance(handler, types.FunctionType):
                GPIO.add_event_callback(self.channel[0], handler)
                # else:
                #     return False
        else:
            # if isinstance(handlers, types.FunctionType):
            GPIO.add_event_callback(self.channel[0], handlers)
            # else:
            #     return False

 
        if self.demand.mode == 'DOUBLE':
            GPIO.output(self.channel[1], True)
            print('たちあげ')
            time.sleep(demand.pulse_time)
            print('たちさげ')
            GPIO.output(self.channel[1], False)
        elif self.demand.mode == 'SINGLE':
            GPIO.output(self.channel[1], self.demand.output_edge)
            if self.demand.output_edge == True:
                self.demand.set_edge(False)
            else:
                self.demand.set_edge(True)
        else:
            print()

        while self.loop_flag:
            print('wait')

        if catch_event.upper() == 'HIGH':
            while GPIO.input(channel[0]) == 0:
                print('waiting event', 1)
        elif catch_event.upper() == 'LOW':
            while GPIO.input(channel[0]) == 1:
                print('waiting event', 0)
        else:
            return GPIO.input(self.channle[0])


        GPIO.remove_event_detect(self.channel[0])

    def set_loop_flag(self, value):
        self.loop_flag = value

    def exception_method(self):
        GPIO.remove_event_detect(self.channel[0])
        GPIO.cleanup(self.channel)
