#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
import smbus
from smbus_sensor_conf import SmbusSensorConf
from event_driven_io import EventDrivenIo
from sensor_exception import SensorException
from event_handler import EventHandler

class EventGpioSensor(SmbusSensorConf, EventDrivenIo, SensorException):
    """This class is for the event driven sensors"""

    def __init__(self, address=None, bus=1):
        super().__init__(address, bus)
        self.event_handler = EventHandler()

    def add_event_handler(self, event, handler):
        # This method is for add event handler.
        # eventを指定して、そのイベントにメソッドを追加する
        self.event_handler.add(event, handler)


    def run(self, read_mode, read_cdm, read_blocks):
        while True:
            # ポーリングで特定のレジスタを読んでくる
            # センサーで読み取ってくる値 = イベントの値
            # ここでの問題は計算式に入れる前の値をセンサーはとってくるので、イベントをしっかり設定する必要あり
            self.sensor_value = self.read(read_mode, read_cmd, read_blocks)
            #この間に計算式を入れて得られた値をeventとして探す方法でもあり
            if self.sensor_value in event_handler.events.keys():
                # keyの中に取得してきた値があれば、そのキーに対応したメソッドをよぶ
                self.event_handler(self.sensor_value)
            else:
                # otherをキーとするメソッドを呼ぶ
                self.event_handler('other')

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


    def remove_event_handler(self, event):
        self.event_handler(event)

    def exception_method(self):
        self.event_handler(event)
