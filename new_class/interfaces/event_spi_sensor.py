#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
import spidev
from spi_sensor_conf import SpiSensorConf
from event_driven_io import EventDrivenIo
from sensor_exception import SensorException
from event_handler import EventHandler


class EventSpiSensor(SpiSensorConf, EventDrivenIo, SensorException):
    """This class is for the event driven sensors"""

    def __init__(self, device=0, bus=0):
        super().__init__(device, bus)
        self.event_handlers = EventHandler()

    def add_event_handler(self, event, handler):
        # This method is for add event handler.
        # eventを指定して、そのイベントにメソッドを追加する
        self.event_handlers.add(event, handler)

    def run(self, sensor_method):
        while True:
            # ポーリングで特定のレジスタを読んでくる
            # センサーで読み取ってくる値 = イベントの値
            # ここでの問題は計算式に入れる前の値をセンサーはとってくるので、イベントをしっかり設定する必要あり
            assert read_method is not None, 'Please gave sensing method.'
            self.sensor_value = sensor_method() # ユーザ定義のセンシングメソッドを実行
            if self.sensor_value in self.event_handlers.events.keys():
                # keyの中に取得してきた値があれば、そのキーに対応したメソッドをよぶ
                self.event_handlers(self.sensor_value)
            else:
                # それ以外の場合otherをキーとするメソッドを呼ぶ
                self.event_handlers('other')

    def read(self, addr, byte=1):
        return self.spi.readByte(addr, byte)

    def write(self, addr, byte=1, values, mode='byte'):
        if mode == 'byte':
            self.spi.writeBytes(addr, values)
        elif mode == 'xfer'
            return self.xfer2(values)

    def remove_event_handler(self, event):
        self.event_handlers.remove()

    def sensor_method(self):
        # 値を取得するセンシングメソッドを記述
        pass

    def exception_method(self):
        self.event_handlers.remove()
        self.spi.close()
