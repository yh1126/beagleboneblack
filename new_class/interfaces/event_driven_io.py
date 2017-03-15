#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from abc import ABCMeta


class EventDrivenIo(metaclass=ABCMeta):
    """This class is for the event driven sensors"""

    @abstractmethod
    def add_event_handler(self, handlers):
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

    __iadd__ = add_event_handler
    __call__ = call_event_handler
    __isub__ = remove_evnet_handler
