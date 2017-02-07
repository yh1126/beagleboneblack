#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
from event_gpio_sensor import EventGpioSensor


class MotionSensorEvent(EventGpioSensor):
    def __init__(self):
        super().__init__(18, 'BCM')
        self.user_method = [self.user_method1, self.user_method2]

    def main(self):
        super().add_event_handler(self.user_method, 'high')

        while True:
            try:
                print('検知中')
                time.sleep(0.1)
            except:
                super().exception_method()

    def user_method1(self):
        print('call user method')

    def user_method2(self):
        print('hello, world')

GPIO.cleanup()
m = MotionSensorEvent()
m.main()
