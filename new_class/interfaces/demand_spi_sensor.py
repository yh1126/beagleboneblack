#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from abc import ABCMeta
import time
import types
import spidev
import RPi.GPIO
from spi_sensor_conf import SpiSensorConf
from demand_driven_io import DemandDrivenIo
from sensor_exception import SensorException
from demand import Demand
from event_handler import EventHandler

class DemandSpiSensor(SpiSensorConf, DemandtDrivenIo, SensorException):
    """This class is for the demand driven sensors"""

    def __init__(self, device=0, bus=0):
        super().__init__(self, device, bus)
        self.event_handlers = EventHandler()

    def demand_issue(self, demand, **catch_event)
        self.sensor_data = [] # 読み取ってとってくる値を取得
        if isinstance(demand, Demand):
            demand = Demand()
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
                self.sensor_data.append(self.sensor_value)

        self.event_handlers.remove()
        return self.sensor_data

    def read(self, addr, byte=1):
        return self.spi.readByte(addr, byte)

    def write(self, addr, byte=1, *values, mode='byte'):
        if mode == 'byte':
            self.spi.writeBytes(addr, values)
        elif mode == 'xfer'
            return self.xfer2(values)

    def exception_method(self):
        self.spi.close()
        self.event_handlers.remove()
