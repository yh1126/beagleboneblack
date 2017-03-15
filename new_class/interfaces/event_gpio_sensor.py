#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO
from gpio_sensor_conf import GpioSensorConf
from event_driven_io import EventDrivenIo
from sensor_exception import SensorException


class EventGpioSensor(GpioSensorConf, EventDrivenIo, SensorException):
    """This class is for the event driven sensors"""

    def __init__(self, channel, pin_mode):
        super().__init__(channel, pin_mode)

    def add_event_handler(self, handlers, edge='HIGH'):
        # This method is for add event handler.

        if edge == 'HIGH':
            GPIO.add_event_detect(self.channel, GPIO.RIGING)
        elif edge == 'LOW':
            GPIO.add_event_detect(self.channel, GPIO.FALLING)
        elif edge == 'BOTH':
            GPIO.add_event_detect(self.channel, GPIO.BOTH)
        else:
            return False

        if isinstance(handlers, list):
            for handler in handlers:
                GPIO.add_event_callback(self.PIN, handler)
        else:
            GPIO.add_event_callback(self.PIN, handlers)

    def remove_event_handler(self):
        GPIO.remove_event_detect(self.channel)

    def exception_method(self):
        GPIO.cleanup(self.channel)
        GPIO.remove_event_detect(self.channel)

    __iadd__ = add_event_handler
    __isub__ = remove_evnet_handler
