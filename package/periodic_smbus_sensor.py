#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from abc import ABCMeta
import time
import types 
import smbus
from smbus_sensor_conf import SmbusSensorConf
from periodci_io import PeriodicIo
from sensor_exception import SensorException
from event_handler import EventHandler

class PeriodicSmbusSensor(SmbusSensorConf, PeriodicIo, Sensorexception):
    """This class is for the periodically driven sensors"""

    def __init__(self, address=None, bus=1, interval=0.5, loop_flag=1):
        assert address is not None, 'Please select address.'
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

        super().__init__(self, address, bus)

    def periodic_read(self, methods):
        # this method is for the sensor to periodically read value.
        # make a thread.
        self.sensor_thread = threading.Thread(target=self.sensor_method, args=(methods))

    def sensor_method(self, methods):
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
        print('called exception method')
