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
import upload
import led
from multiprocessing import Pool
from multiprocessing import Process
from multiprocessing import Queue #データの共有を行える FIFO

class Manager:

  def __init__(self):
    self.evt    = event.Event()
    self.motion = motion.Motion() #sencor class
    self.shoot  = shoot.Shoot() #actuator class
    self.upload = upload.Upload() #actuator class
    self.led    = led.led()

  def execute(self, earg=None):
    self.evt(self, earg)

  def execute1(self, earg=None):
    self.led.execute(self, earg)

  def main(self):
    self.ps = [
      Process(target=self.execute1),
      Process(target=self.execute)
      #Process(target=self.execute)
    ]
    for p in self.ps:
      p.start()
      #p.join()
    

if __name__ == '__main__':
  man  = Manager()
  man.evt += man.motion.execute
  man.motion.evt += man.shoot.execute
  man.motion.evt += man.upload.execute
  #man.execute()
  man.main()
