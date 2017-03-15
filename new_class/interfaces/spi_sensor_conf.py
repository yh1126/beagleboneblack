#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from abc import ABCMeta
import spidev


class SpiSensorConf(metaclass=ABCMeta):
    """This class has spi interface Conf."""

    def __init__(self, device=0, bus=0):

        if device == 0 or device == 1:
            self.device = device
            print('Select device is', device)
        else:
            print('Please secelet device 0 or 1.')
            return False

        if bus == 0 or bus == 1:
            self.bus = bus
        else:
            print('please select bus number 0 or 1.')
            return False

        self.spi = spidev.SpiDev()
        self.spi.open(bus, device)

    def __del__(self):
        self.spi.close(self.bus, self.device)
        print('del')

t = SpiSensorConf(12)
