#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from abc import ABCMeta
import time
import types
import smbus
from gpio_sensor_conf import GpioSensorConf
from event_driven_io import EventDrivenIo
from sensor_exception import SensorException
from demand import Demand


class DemandSmbusSensor(GpioSensorConf, EventDrivenIo, SensorException):
    """This class is for the demand driven sensors"""

    def __init__(self, demand, address=None, bus=1):
        super().__init__(self, address, bus)

    def demand_issue(self, demand, **handlers):
        if isinstance(demand, Demand):
            demand = Demand()
        else:
            print('Please give a Demand object.')
            return False

        if demand.mode == 'CMD':
            for handler_key in handlers.keys():
                if isinstance(handler_key, int):
                    pass
                else:
                    print(handler_key, 'is not supported.')
                    return False

            for handler_value in handlers.keys():
                if isinstance(handler_valuem types.FunctionType):
                    pass
                else:
                    print(handler_value, 'is not supported.')
                    return False
        else:
              return False

        self.handler_keys   = list(handlers.keys())
        self.handler_values = list(handlers.values())
        self.handlers = handlers

        # 一度だけ書き込むのか、それとも呼び出されるたび書き込むのか？
        self.write(demand.write_value, demand.write_mode, demand.write_cmd)
        time.sleep(demand.interval)
        self.sensor_value = self.read(demand.read_mode, demand.read_cmd, read_blocks)

        # どんな値であっても特定のメソッドを呼ぶケース
        # ある値であるメソッドを呼ぶケース
        if self.sensor_value in handler_keys:
            # keyの中に取得してきた値があれば、そのキーに対応したメソッドをよぶ
            self.handlers[self.sensor_value]()
        else:
            # anyをキーとするメソッドを呼ぶ
            self.handlers['any']()

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
          GPIO.remove_event_detect(self.channels[0])
          GPIO.cleanup(self.channels)
