#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
from event_gpio_sensor import EventGpioSensor


class EventGpioTemplate(EventGpioSensor):
    def __init__(self):
        super().__init__(pin_number)
        self.user_methodd = [user_method1, user_method2]

    def main_method(self):
        # add event handler. gave methods and detect edge.
        # edge can receive 'high', 'low', 'both'.
        super().add_event_handler(self, user_methods, 'high')

        while True:
            try:
                # describe your code.
                pass
            else:
                super().exception_method()

    def user_method1(self):
        pass

    def user_method2(self):
        pass
