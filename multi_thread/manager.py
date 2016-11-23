#!/usr/local/bin/python
# -*- coding: utf-8 -*-
###/usr/bin/python

import pysftp
import time
import RPi.GPIO as GPIO
import os
import datetime
import event
import motion
import shoot
import uploader
import threading
import sonic_sensor

rlock = threading.RLock() # lock object

class Manager:

  def __init__(self):
     self.evt         = event.Event()
     self.motion      = motion.Motion() #actuator class
     self.sonic       = sonic_sensor.SonicSensor()
     self.shoot       = shoot.Shoot() #sencer class
     self.uploader    = uploader.Uploader() #sencer class
     self.motion.evt += self.shoot.execute
     self.motion.evt += self.uploader.execute
     self.sonic.evt  += self.shoot.execute
     self.sonic.evt  += self.uploader.execute 

  def execute(self):
    #self.motion.execute(self, None)
    self.sonic.measure(self, None)

if __name__ == '__main__':
  man  = Manager()
  man.execute()
