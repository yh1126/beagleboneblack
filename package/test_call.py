# -*- coding: utf-8 -*-

from event_handler import EventHandler

def test1(earg=None):
  print('test1')

def test2(earg=None):
  print('test2')

evt = EventHandler()
evt.add_event_handler('str', test1)
