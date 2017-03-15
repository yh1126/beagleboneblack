#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import threading
import time
import smbus
from smbus_sensor_conf import SmbusSensorConf
from event_driven_io import EventDrivenIo
from sensor_exception import SensorException
from event_handler import EventHandler


class EventSmbusSensor(SmbusSensorConf, EventDrivenIo, SensorException):
    """This class is for the event driven sensors"""

    def __init__(self, address=None, bus=1):
        assert address is not None, 'Please select address.'
        super().__init__(address, bus)
        self.event_handlers = EventHandler()

    def add_event_handler(self, event, handler):
        # eventを指定して、そのイベントにメソッドを追加する
        self.event_handlers.add(event, handler)

    def run(self):
        self.sensor_thread = threading.Thread(target=self.sensor_method, args())
    def sensor_method(self, user_method):
        # センシングメソッドを与える, 与えたメソッドを呼ぶ得られた値がイベントとしてあるか調べる
        while True:
            # ポーリングで特定のレジスタを読んでくる
            # センサーで読み取ってくる値 = イベントの値
            assert read_method is not None, 'Please gave sensing method.'
            self.sensor_value = sensor_method() # ユーザ定義のセンシングメソッドを実行
            if self.sensor_value in event_handler.events.keys():
                # keyの中に取得してきた値があれば、そのキーに対応したメソッドをよぶ
                self.event_handlers(self.sensor_value)
            else:
                # それ以外の場合otherをキーとするメソッドを呼ぶ
                self.event_handlers('other')

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


    def remove_event_handler(self, event):
        self.event_handlers.remove()

    def user_method(self):
        # 値を取得するセンシングメソッドを記述
        pass

    def exception_method(self):
        self.event_handlers.remove()
