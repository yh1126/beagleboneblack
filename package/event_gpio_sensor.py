#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO
from gpio_sensor_conf import GpioSensorConf
from event_driven_io import EventDrivenIo
from sensor_exception import SensorException


class EventGpioSensor(GpioSensorConf, EventDrivenIo, SensorException):
    """This class is for the event driven sensors"""

    def __init__(self, channel, pin_mode='BCM'):
        super().__init__(channel, pin_mode)

    def add_event_handler(self, handlers, edge='HIGH'):
        # This method is for add event handler.

        if edge.upper() == 'HIGH':
            GPIO.add_event_detect(self.channel[0], GPIO.RISING)
        elif edge.upper() == 'LOW':
            GPIO.add_event_detect(self.channel[0], GPIO.FALLING)
        elif edge.upper() == 'BOTH':
            GPIO.add_event_detect(self.channel[0], GPIO.BOTH)
        else:
            return False

        if isinstance(handlers, list):
            for handler in handlers:
                GPIO.add_event_callback(self.channel[0], handler)
        else:
            GPIO.add_event_callback(self.channel[0], handlers)

    def call_event_handler(self):
        pass

    def remove_event_handler(self):
        GPIO.remove_event_detect(self.channel[0])

    def exception_method(self):
        GPIO.cleanup(self.channel[0])
        GPIO.remove_event_detect(self.channel[0])
