#!/usr/local/bin/python
# -*- coding: utf-8 -*-
###/usr/bin/python

import pysftp
import time
import RPi.GPIO as GPIO
import os
import datetime
import event

class Manager:



  def __init__(self):
    self.INTAVAL = 3
    self.SLEEPTIME = 2
    self.SENSOR_PIN = 18
    self.HOST = '172.21.42.152'
    self.PORT = 22
    self.USER = 'iwatalab'
    self.PRIVATE_KEY_FILE = '/home/pi/.ssh/id_rsa'
    self.name = ''
    self.uploadPath = '/home/iwatalab/upload_image'
    self.evt = event.Event()
    self.todaydetail = datetime.datetime.today()

  def execute(self):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.SENSOR_PIN, GPIO.IN)
    self.st = time.time()-self.INTAVAL
    while True:
      print("待機中")
      if(GPIO.input(self.SENSOR_PIN)==GPIO.HIGH) and (self.st + self.INTAVAL < time.time()):
        print ("人を感知しました")
        self.st = time.time()
        self.evt(self)
      time.sleep(self.SLEEPTIME)
    GPIO.cleanup()


def handle_shoot(self, earg):
  self.todaydetail = datetime.datetime.today().strftime("%Y%m%d_%H%M%S")
  print self.todaydetail
  os.system('raspistill -o ' + self.todaydetail + '.jpg -vf -hf -w 1024 -h 768 -t 1000 -ex antishake')
  time.sleep(2)

def handle_upload(self, earg):
  self.fPath = '/home/pi/surcamera/' + self.todaydetail + '.jpg'
  sftp = pysftp.Connection(self.HOST, username=self.USER, port=self.PORT, private_key=self.PRIVATE_KEY_FILE)
  sftp.listdir()
  sftp.chdir(self.uploadPath)
  sftp.getcwd()
  sftp.put(self.fPath)
  for item in sftp.execute('ls -l /home/iwatalab/upload_image'):
    print item,     #結果を表示

  sftp.close()

if __name__ == '__main__':
  man  = Manager()
  man.evt += handle_shoot
  man.evt += handle_upload
  man.execute()


