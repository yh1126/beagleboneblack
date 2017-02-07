#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class SensorException(metaclass=ABCMeta):
    """This class has exception method for sensors of each I/F."""

    @abstractmethod
    def exception_method(self):
        # subclass implement this method.
        pass
