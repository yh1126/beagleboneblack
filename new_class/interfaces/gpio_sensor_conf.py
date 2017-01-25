#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from abc import ABCMeta

# 'import RPi.GPIO as GPIO


class GpioSensorConf(metaclass=ABCMeta):
    """This class has gpio interface conf."""

    def __init__(self, channel=None, mode='BCM'):

        assert channel is not None, 'Please select channel.'
        # Noneのようなシングルトンと比較する時は等価演算子は使っちゃだめ

        if isinstance(channel, int):
            self.channel = channel
            print('Select', channel, 'pin')
        elif isinstance(channel, list):
            self.channel = channel
            print('Select', *channel, 'pin')
        else:
            print('Please give a value of int or list.')
            return False

        if mode == 'BCM':
            print('select BCM mode.')
            GPIO.setmode(GPIO.BCM)
        elif mode == 'BOARD':
            print('select BOARD mode.')
            GPIO.setmode(GPIO.BOARD)
        else:
            return False

    def __del__(self):
        print('instance is del')
        GPIO.remove_event_detect(self.channel)
        GPIO.cleanup(self.channel)

val = [1, 2]
t = GpioSensorConf(val)
print(t.__doc__)
