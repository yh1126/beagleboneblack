#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from abc import ABCMeta
import time
import types 
import spidev
from spi_sensor_conf import SpiSensorConf
from periodci_io import PeriodicIo
from sensor_exception import SensorException
from event_handler import EventHandler

class PeriodicSmbusSensor(SpiSensorConf, PeriodicIo, Sensorexception):
    """This class is for the periodically driven sensors"""

    def __init__(self, device=0, bus=0, interval=0.5, loop_flag=1):
        self.event_handler = EventHandler()
        if isinstance(interval, int):
            self.loop_interval  = interval
        elif isinstance(interval, float):
            self.loop_interval  = interval
        else:
            print(interval, 'is not suppoerted. Please give an integer or float interval value.')

        if loop_flag == True or loop_flag == False:
            self.loop_flag = loop_flag
        else:
            print(loop_flag, 'is not suppoerted. Please give a False(0) or True(1).')

        super().__init__(self, device, bus)

    def periodic_read(self, *methods):
        # methods is tuple
        # this method is for the sensor to periodically read value.
        for method in methods:
            if isinstance(method, types.FunctionType):
                pass
            else:
                print(m, 'is not supported. Please give a function.')

        while:
            try:
                for method in methods:
                    method()
                time.sleep(self.loop_interval)
            except:
                exception_method()

    def read(self, addr, byte=1):
        return self.spi.readByte(addr, byte)

    def write(self, addr, byte=1, values=None, mode='byte'):
        if mode == 'byte':
            self.spi.writeBytes(addr, values)
        elif mode == 'xfer'
            return self.xfer2(values)

    def set_interval(self, interval):
        if isinstance(interval, int):
            self.loop_interval  = interval
            return loop_interval
        elif isinstance(interval, float):
            self.loop_interval  = interval
            return loop_interval
        else:
            print(interval, 'is not suppoerted. Please give an integer or float interval value.')
            return False

    def set_loop_flag(self, loop_flag):
        if loop_flag == True or loop_flag == Flase:
            self.loop_flag = loop_flag
        else:
            print(loop_flag, 'is not suppoerted. Please give a False(0) or True(1).')

    def exception_method(self):
        self.spi.close()
        print('called exception method')
