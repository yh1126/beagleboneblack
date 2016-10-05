#!/usr/local/bin/python
# -*- coding: utf-8 -*-
###/usr/bin/python

import pysftp
import time
import RPi.GPIO as GPIO
import os
import datetime
import event #created
import motion
import shoot
import upload

class Manager:

  def __init__(self):
    self.evt    = event.Event()
    self.motion = motion.Motion() #special class
    self.shoot  = shoot.Shoot() #nomal class
    self.upload = upload.Upload() #nomal class

  def execute(self):
    self.evt(self)

if __name__ == '__main__':
  man  = Manager()
  man.motion.evt
  man.evt += man.motion.execute()
  man.motion.evt += man.shoot.execute()
  man.motion.evt += man.upload.execute()
  man.execute()


