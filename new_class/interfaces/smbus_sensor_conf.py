#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from abc import ABCMeta
import smbus


class SmbusSensorConf(metaclass=ABCMeta):
    """This class has i2c interface conf."""

    def __init__(self, address=None, bus=1):

        assert address is not None, 'Please select address.'

        if isinstance(address, int):
            self.address = address
            print( address, 'address selected.')
        else:
            print('Please give a address value of int!!')
            return False

        if bus == 1:
            self.i2c = smbus.Smbus(bus)
        elif bus == 0:
            self.i2c = smbus.Smbus(bus)
        else:
            print('This Value is not support.')
            return False

    def __del__(self):
        print('del')

t = SmbusSensorConf(12)
