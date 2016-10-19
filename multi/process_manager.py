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
from multiprocessing import Pool
from multiprocessing import Process
from multiprocessing import Queue #データの共有を行える FIFO
class Manager:

  def __init__(self):
    self.evt    = event.Event()
    self.motion = motion.Motion() #actuator class
    self.shoot  = shoot.Shoot() #sencer class
    self.upload = upload.Upload() #sencer class

  def execute(self, earg=None):
    self.evt(self, earg)

  def main():
    self.process = Pool(2)
    

if __name__ == '__main__':
  man  = Manager()
  man.evt += man.motion.execute
  man.motion.evt += man.shoot.execute
  man.motion.evt += man.upload.execute
  man.execute()
