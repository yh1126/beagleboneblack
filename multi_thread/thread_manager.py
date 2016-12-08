#!/usr/local/bin/python
# -*- coding: utf-8 -*-
###/usr/bin/python

import pysftp
import time
import RPi.GPIO as GPIO
import os
import datetime
import event
import motion_sensor
import sonic_sensor
import camera
import uploader
import led
import threading
import sonic_sensor

#capture_lock = threading.RLock() # lock object
#up_lock = threading.RLock() # lock object

class Manager:
  def __init__(self):
    self.evt    = event.Event()
    self.camera  = camera.Camera() #actuator class
    self.uploader = uploader.Uploader() #actuator class
    self.led    = led.Led()
    self.motion = motion_sensor.MotionSensor() #sencor class
    self.sonic  = sonic_sensor.SonicSensor() #sensor class
    self.motion.event_handlers += self.camera.shutter
    self.motion.event_handlers += self.uploader.execute
    self.sonic.evt += self.camera.shutter
    self.sonic.evt += self.uploader.execute

  def motion_method(self, earg=None):
    print "=== start motion_thread ===="
    print "[%s] thread (method) : " % threading.currentThread().getName() + str(datetime.datetime.today())
    self.motion.detect(self, earg)
    print "=== end motion_thread (method) ==="

  def sonic_method(self, earg=None):
    print "=== start sonic_thead ===="
    print "[%s] thread (method) : " % threading.currentThread().getName() + str(datetime.datetime.today())
    self.sonic.measure(self, earg)
    print "=== end sonic_thread (method) ==="

  def test(self, earg=None):
    print "=== start test_thread(method) ===="
    print "[%s] thread (method) : " % threading.currentThread().getName() + str(datetime.datetime.today())
    for i in range(earg):
      print "hello, %d" % i
      time.sleep(1)
    print "=== end [%s] test_thread (method) ===" % threading.currentThread().getName()

  def main(self):
    try: 
      sonic_thread  = threading.Thread(target=self.sonic_method, name="sonic_sensor_thread", args=(5, ))
      motion_thread =  threading.Thread(target=self.motion_method, name="motion_sensor_thread", args=(5, ))

      motion_thread.start()
      time.sleep(0.001)
      sonic_thread.start()

      motion_thread.join()
      sonic_thread.join()
      print("finished prgram")
      GPIO.cleanup

    except:
      print("error:finished prgram")
      GPIO.cleanup

if __name__ == '__main__':
  man  = Manager()
  man.main()

