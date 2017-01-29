#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from abc import ABCMeta
import time
import RPi.GPIO
from gpio_sensor_conf import GpioSensorConf
from event_driven_io import EventDrivenIo
from sensor_exception import SensorException



class DemandDrivenIo(metaclass=ABCMeta):
    """This class is for the demand driven sensors"""

    def __init__(self, channel, mode):
      

    @abstractmethod
    def read(self):
        # subclass implement this method.
        # this method is for the sensor to read value.
        pass

    @abstractmethod
    def write(self):
        # subclass implement this method.
        # this method is for the sensor to write value.
        pass
