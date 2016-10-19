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

class Manager:

  def __init__(self):
     self.evt    = event.Event()
     self.motion = motion.Motion() #actuator class
     self.shoot  = shoot.Shoot() #sencer class
     self.upload = upload.Upload() #sencer class

  def execute(self):
    self.evt(self)

  def main(self)
    self.ps = [
      Process(target=self.execute),
#      Process(target=self.extcute),
#      Process(target=self.extcute),
#      Process(target=self.extcute)
    ]
    for p in self.ps:
      p.start()
      p.join()#joinがなんなのかよくわかってない


if __name__ == '__main__':
  man  = Manager()
  man.evt += man.motion.execute
  man.motion.evt += man.shoot.execute
  man.motion.evt += man.upload.execute
#  man.execute()
  man.main()
