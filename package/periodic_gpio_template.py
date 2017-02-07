#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
from periodic_gpio_sensor import PeriodicGpioSensor


class PeriodicGpioTemplate(PeriodicGpioSensor):
    def __init__(self):
        super().__init__(pin_number, loop_interval)
        self.user_method = [self.ensor_method, self.test_method]
        self.handler = [self.handler1, self.handler2]
        self.key

        # key指定し、self.sensor_valueにkeyと同じ値が入ったとき
        # user_methodを逐次的に呼び出していく
        super().add_event_handler(self.key, self.handler)

    def main(self):
        super().periodic_read(user_method)

    def sensor_method(self):
        # describe your code
        # e.g self.key = GPIO.input[self.chennle[0]]
        self.sensor_value = self.key
        # センサーメソッド実行後、sensor_valueの値を確認
        # 値がevent_handlerのキーとして存在すれば、ハンドラを呼びに行く
        pass

    def test_method(self):
        pass

    def handler1(self):
        pass

    def handler2(self):
        pass
