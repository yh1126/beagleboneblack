#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from abc import ABCMeta
import time↲
import RPi.GPIO↲
from gpio_sensor_conf import GpioSensorConf↲
from periodci_io import PeriodicIo↲
from sensor_exception import SensorException↲
from event import Event
# validation用のモジュールを追加したら楽？

class PeriodicIo(GpioSensorConf, PeriodicIo, Sensorexception, metaclass=ABCMeta):
    """This class is for the periodically driven sensors"""

    def __init__(self, channel, mode, interval=0.5, loop_flag=1):
        self.loop_interval  = interval
        self.loop_flag      = loop_flag
        self.event_handlers = Event()
        super().__init__(self, channel, mode)

    # def read(self):
    #     return GPIO.input(self.channel)

    @abstractmethod
    def periodic_read(self, *method):
        # this methos is for the sensor to periodically read value.
        while:
            time.sleep(self.loop_interval)
        pass

    def set_interval(self, value):
          self.loop_interval = value
          return loop_interval

    def set_loop_flag(self, value):
       if value == 0 or value == 1:
            self.loop_flag = value
            return loop_flag
      else:
            print('Please give 0 or 1')
