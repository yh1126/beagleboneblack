#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from abc import ABCMeta
import time
import types
import threading
import RPi.GPIO as GPIO
from gpio_sensor_conf import GpioSensorConf
from periodic_io import PeriodicIo
from sensor_exception import SensorException
from event_handler import EventHandler


class PeriodicGpioSensor(GpioSensorConf, PeriodicIo, SensorException, EventHandler):
    """This class is for the periodically driven sensors"""

    def __init__(self, channel, interval=0.5, loop_flag=1, pin_mode='BCM'):
        super().__init__(channel, pin_mode)
        self.event_handler = EventHandler()
        self.sensor_value = None

        if isinstance(interval, int):
            self.loop_interval = interval
        elif isinstance(interval, float):
            self.loop_interval = interval
        else:
            print(interval, 'is not suppoerted.')
            print('Please give an integer or float interval value.')

        if loop_flag == True or loop_flag == False:
            self.loop_flag = loop_flag
        else:
            print(loop_flag, 'is not suppoerted.')
            print('Please give a False(0) or True(1).')

    def sensor_method(self, *methods):
        print(methods)
        while self.loop_flag:
            try:
                print(1)
                print(self.event_handler.events)
                for method in methods:
                    method()
                    # methodないでself.sensor_valueに値が入れられれば
                    # イベントハンドラを呼ぶ

                if self.sensor_value is not None:
                    self.event_handler(self.sensor_value)

                time.sleep(self.loop_interval)
            except:
                self.exception_method()

    def periodic_read(self, methods):
        # this method is for the sensor to periodically read value.
        # make a thread.
        print('make a sensor thred')
        self.sensor_thread = threading.Thread(target=self.sensor_method, args=(methods,))
        self.sensor_thread.start()

    def set_interval(self, interval):
        if isinstance(interval, int):
            self.loop_interval = interval
            return loop_interval
        elif isinstance(interval, float):
            self.loop_interval = interval
            return loop_interval
        else:
            print(interval, 'is not suppoerted.')
            print('Please give an integer or float interval value.')
            return False

    def set_loop_flag(self, loop_flag):
        if loop_flag == True or loop_flag == Flase:
            self.loop_flag = loop_flag
        else:
            print(loop_flag, 'is not suppoerted.')
            print('Please give a False(0) or True(1).')

    def exception_method(self):
        GPIO.cleanup(self.channel)
        self.event_handler.remove_event_handler
