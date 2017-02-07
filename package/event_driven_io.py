#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class EventDrivenIo(metaclass=ABCMeta):
    """This class is for the event driven sensors"""

    @abstractmethod
    def add_event_handler(self):
        # subclass implement this method.
        # This method is for add event handler.
        pass

    @abstractmethod
    def call_event_handler(self):
        # subclass implement this method.
        # This method is for add event handler.
        pass

    @abstractmethod
    def remove_event_handler(self):
        # subclass implement this method.
        # This method is for add event handler.
        pass
