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
import threading

class Manager:

  def __init__(self):
    self.evt    = event.Event()
    self.motion = motion.Motion() #sencor class
    self.shoot  = shoot.Shoot() #actuator class
    self.upload = upload.Upload() #actuator class
    self.led    = led.Led()

  def execute(self, earg=None):
    print "=== start thread1(method) ===="
    print "[%s] thread (method) : " % threading.currentThread().getName() + str(datetime.datetime.today())
    self.evt(self, earg)

  def execute1(self, earg=None):
    print "=== start thread1(method) ===="
    print "[%s] thread (method) : " % threading.currentThread().getName() + str(datetime.datetime.today())
    self.led.execute(self, earg)
    print "=== end [%s] thread (method) ===" % threading.currentThread().getName()

  def test(self, earg=None):
    print "=== start thread1(method) ===="
    print "[%s] thread (method) : " % threading.currentThread().getName() + str(datetime.datetime.today())
    for i in range(earg):
      print "hello, %d" % i
      time.sleep(1)
    print "=== end [%s] thread (method) ===" % threading.currentThread().getName()

  def main(self):
#    thread_motion = threading.Thread(target=self.execute, name="motion_sensor_class",)
    thread_led = threading.Thread(target=self.execute1, name="temp_sensor_class", )
    thread_test = threading.Thread(target=self.test, name="test_sensor_class", args=(5, ))

#    thread_motion.start()
    thread_test.start()
    time.sleep(1)
    thread_led.start()

if __name__ == '__main__':
  man  = Manager()
  man.evt += man.motion.execute
  man.motion.evt += man.shoot.execute
  man.motion.evt += man.upload.execute
  #man.execute()
  man.main()

