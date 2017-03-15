#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
from periodic_gpio_sensor import PeriodicGpioSensor


class PeriodicGpioTemplate(PeriodicGpioSensor):
    def __init__(self):
        super().__init__(pin_number, loop_interval)
        self.user_method = [self.user_method1, self.user_method2]
        self.handler = [self.handler1, self.handler2]
        self.key

        super().add_event_handler(self.key, self.handler)

    def run_sensor(self):
        super().periodic_read(user_method)

    def user_method(self):
        # e.g self.key = GPIO.input[self.chennle[0]]
        self.sensor_value = self.key
        # センサーメソッド実行後、sensor_valueの値を確認
        # 値がevent_handlerのキーとして存在すれば、ハンドラを呼びに行く
        pass

    def user_method(self):
        pass

    def handler1(self):
        pass

    def handler2(self):
        pass
