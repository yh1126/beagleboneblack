#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from abc import ABCMeta


class GpioSensorConf(metaclass=ABCMeta):
    """This class has gpio interface conf."""

    def __init__(self, channel=None, mode='BCM'):

        assert channel is not None, 'Please select channel.'
        # Noneのようなシングルトンと比較する時は等価演算子は使っちゃだめ

        if mode.upper() == 'BCM':
            print('select BCM mode.')
            GPIO.setmode(GPIO.BCM)
        elif mode.upper() == 'BOARD':
            print('select BOARD mode.')
            GPIO.setmode(GPIO.BOARD)
        else:
            return False

        if isinstance(channel, int):
            self.channel = [channel]
            print(type(self.channel))
            print(channel, 'pin selected.')
            GPIO.setup(self.channel[0], GPIO.IN)
        elif isinstance(channel, list):
            self.channel = channel
            print(channel[0], 'is input channel.')
            print(channel[1], 'is output channel.')
            GPIO.setup(self.channel[0], GPIO.IN)
            GPIO.setup(self.channel[1], GPIO.OUT)
        else:
            print('Please give an integer addressor.')
            return False


    def __del__(self):
        print('instance is del')
        # GPIO.cleanup(self.channel[0])
