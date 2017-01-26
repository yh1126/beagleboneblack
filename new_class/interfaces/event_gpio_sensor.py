#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO
from gpio_sensor_conf import GpioSensorConf
from event_driven_io import EventDrivenIo
from sensor_exception import SensorException


class EventGpioSensor(GpioSensorConf, EventDrivenIo, SensorException):
    """This class is for the event driven sensors"""

    def __init__(self):
        

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

        if isinstance(handlers, list):↲
            for handler in handlers:↲
                GPIO.add_event_callback(self.PIN, handler)↲
        else:↲
            GPIO.add_event_callback(self.PIN, handlers)↲

    def call_event_handler(self):
        # このメソッドはGPIOのevent駆動のセンサーでは実装する必要がない
        pass

    def remove_event_handler(self):
        GPIO.remove_event_detect(self.channel)

    __iadd__ = add_event_handler
    __isub__ = remove_evnet_handler
