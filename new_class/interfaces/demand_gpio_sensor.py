#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from abc import ABCMeta
import time
import types
import RPi.GPIO
from gpio_sensor_conf import GpioSensorConf
from demand_driven_io import DemandDrivenIo
from sensor_exception import SensorException
from demand import Demand


class DemandGpioSensor(GpioSensorConf, DemandDrivenIo, SensorException):
    """This class is for the demand driven sensors"""

    def __init__(self, demand, channels. pin_mode='BCM'):
        super().__init__(self, channels, pin_mode)

    def demand_issue(self, demand, handlers, catch_event=None):
        if isinstance(demand, Demand):
            demand = Demand()
        else:
            print('Please give a Demand object.')
            return False

        if demand.mode == 'DOUBLE':
            GPIO.output(self.channels[1], True)
            time.sleep(demand.interval)
            GPIO.output(self.channels[1], False)
        elif demand.mode == 'SINGLE':
            GPIO.output(self.channels[1], demand.output_edge)
            if demand.output_edge == True:
                demand.set_edge(False)
            else:
                demand.set_edge(True)

        if catch_event == 'HIGH':
            GPIO.add_event_detect(self.channel[0], GPIO.RISING)
        elif catch_event == 'LOW':
            GPIO.add_event_detect(self.channel[0], GPIO.FAILING)
        elif catch_event == 'BOTH':
            GPIO.add_event_detect(self.channel[0], GPIO.BOTH)
        else:
            return GPIO.input(self.channle[0])

      if isinstance(handlers, list):
          for handler in handlers:
              if isinstance(handler, types.FunctionType):
                  GPIO.add_event_callback(self.channels[0], handler)
              else:
                  return False
      else:
          GPIO.add_event_callback(self.channels[0], handler)

      GPIO.remove_event_detect(self.channels[0])
      GPIO.cleanup(self.channels)

      def exception_method(self):
          GPIO.remove_event_detect(self.channels[0])
          GPIO.cleanup(self.channels)
