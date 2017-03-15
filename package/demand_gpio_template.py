#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
from demand_gpio_sensor import DemandGpioSensor
from demand import Demand


class DemandGpioTemplate(DemandGpioSensor):
    def __init__(self):
        super().__init__([pin_number1, pin_number2])
        self.demand = Demand(mode='', event='key', pulse_time=0.0001)
        self.user_methodd = [user_method1, user_method2]
        self.handler = [handler1, handler2]

        # key指定し、self.sensor_valueにkeyと同じ値が入ったとき
        # user_methodを逐次的に呼び出していく
        super().add_event_handler(key, handler)

    def main_method(self):
        super().periodic_read(self, user_method)
        # add event handler. gave methods and detect edge.
        # edge can receive 'hige', 'low', 'both'.
        super().demand_issue(self.demand, sensor_method1, cathc_edge='high')
        self.demand.set_mode(None)
        super().demand_issue(self.demand, sensor_method2, cathc_edge='high')

    def sensor_method1(self):
        # please describe "loop_flag = 0"
        self.loop_flag = 0
        pass

    def sensor_method2(self):
        self.loop_flag = 0
        # イベントハンドラを呼びたいときは以下のようにしてください
        # self.sensor_value = GPIO.input(self.channel[0])
        # または self.sensor_value = value
        # if self.sensor_value in self.event_handler:
        #     self.eent_handler()
        # else:
        #     pass

    def handler1(self):
        pass

    def handler2(self):
        pass
