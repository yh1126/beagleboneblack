# -*- coding: utf-8 -*-

from event_handler import EventHandler

def test1():
  print('test1')

def test2():
  print('test2')
evt = EventHandler()
evt.add('str', test1)
