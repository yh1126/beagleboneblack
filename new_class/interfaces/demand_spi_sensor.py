#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from abc import ABCMeta
import time
import types
import RPi.GPIO
from gpio_sensor_conf import GpioSensorConf
from event_driven_io import EventDrivenIo
from sensor_exception import SensorException
from demand import Demand


class DemandGpioSensor(GpioSensorConf, EventDrivenIo, SensorException):
    """This class is for the demand driven sensors"""

    def __init__(self, demand, channels. pin_mode='BCM'):
        super().__init__(self, channels, pin_mode)

    def demand_issue(self, demand, handlers, catch_edge='HIGH')
        if isinstance(demand, Demand):
            demand = Demand()
        else:
            print('Please give a Demand object.')
            return False

        if demand.mode == 'DOUBLE':
            GPIO.output(self.channels[1], True)
            time.sleep(demand.interval)
            GPIO.output(self.channels[0], False)
        elif demand.mode == 'SINGLE':
            GPIO.output(self.channels[1], demand.edge)
            if demand.edge == True:
                demand.set_edge(False)
            else:
                demand.set_edge(True)

        if catch_edge == 'HIGH':
            GPIO.add_event_detect(self.channel[0], GPIO.RISING)
        elif catch_edge == 'LOW':
            GPIO.add_event_detect(self.channel[0], GPIO.FAILING)
        elif catch_edge == 'BOTH':
            GPIO.add_event_detect(self.channel[0], GPIO.BOTH)
        else:
            return False

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
