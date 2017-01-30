#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
import smbus
from smbus_sensor_conf import SmbusSensorConf
from event_driven_io import EventDrivenIo
from sensor_exception import SensorException


class EventGpioSensor(SmbusSensorConf, EventDrivenIo, SensorException):
    """This class is for the event driven sensors"""

    def __init__(self, address=None, bus=1):
        super().__init__(address, bus)

    def add_event_handler(self, **handlers):
        # This method is for add event handler.
        # 一つイベントハンドラを追加できる
        # 特定のイベント(値)に対して
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
# handlersの例: {'12345': test_method, '1222':(test_method1, test_method2), 'any':any_method}

        # どんな値であっても特定のメソッドを呼ぶケース
        # ある値であるメソッドを呼ぶケース
    def run(self, read_mode, read_cdm, read_blocks):
        self.sensor_value = self.read(read_mode, read_cmd, read_blocks)
        if self.sensor_value in handler_keys:
            # keyの中に取得してきた値があれば、そのキーに対応したメソッドをよぶ
            if isinstance(self.handlers[sensor_value]):
                for method in self.handlers[sensor_value]:
                    method()
            else:
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


    def remove_event_handler(self):
        GPIO.remove_event_detect(self.channel)

    def exception_method(self):
        GPIO.cleanup(self.channel)
        GPIO.remove_event_detect(self.channel)

    __iadd__ = add_event_handler
    __isub__ = remove_evnet_handler
