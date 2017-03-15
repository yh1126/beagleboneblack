#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from abc import ABCMeta
import time
import types
import smbus
from smbus_sensor_conf import SmbusSensorConf
from demand_driven_io import DemandDrivenIo
from sensor_exception import SensorException
from demand import Demand


class DemandSmbusSensor(SmbusSensorConf, DemandDrivenIo, SensorException):
    """This class is for the demand driven sensors"""

    def __init__(self, address=None, bus=1):
        super().__init__(self, address, bus)
        self.event_handlers = EventHandler()

    def demand_issue(self, demand, **catch_event)
        self.sensor_data = [] # 読み取ってとってくる値を格納する箱
        if isinstance(demand, Demand()):
            self.demand = demand
        else:
            print('Please give a Demand object.')
            return False

        if catch_event != {}:
            # cath_eventは{'1011':method} これがもらえるとよそう
            # main処理 書 -> 読 -> コールバック(値に応じた)
            for event in catch_event:
                self.event_handlers.add(event, catch_event[event])

            for write in demand.write_methods():
                write()

            time.sleep(demand.interval)

            for read in demand.read_methods():
                self.sensor_value = read()
                if self.sensor_value in event_handler.events.keys():
                    self.event_handler(self.sensor_value)
                else:
                    self.event_handler('other')

                self.sensor_data.append(self.sensor_value)
        else:
            # catch_event == {}
            for write in demand.write_method():
                write()

            time.sleep(demand.interval)

            for read in demand.read_methods():
                self.sensor_value = read()
                self.sensor_data.append(self.sensor_value)

        self.event_handlers.remove()
        return self.sensor_data


    def read(self, mode='byte', cmd=None, *blocks):
        if mode == 'byte':
            return self.i2c.read_byte(self.address)
        elif mode == 'byte' and cmd != None:
            return self.i2c.read_byte_data(self.address, cmd)
        elif mode == 'block' and cmd != None:
            return self.i2c.read_block_data(self.address, cmd, blocks[0])
        else:
            print('Not Supported data.')
            return False

    def write(value, mode='byte', cmd=None):
        if mode == 'byte':
              self.i2c.write_byte(self.address, value)
        elif mode == 'byte' and cmd != None:
              self.i2c.write_byte_data(self.address, cmd,  value)
        elif mode == 'word' and cmd != None:
              self.i2c.write_word_data(self.address, cmd,  value)
        elif mode == 'process' and cmd != None:
              return self.i2c.process_call(self.address, cmd,  value)
        else:
            return False

      def exception_method(self):
          pass
