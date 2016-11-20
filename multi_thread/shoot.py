#!/usr/local/bin/python
# -*- coding: utf-8 -*-
###/usr/bin/python
# shoot.py
import threading
import os
import time
import datetime

class Shoot(object):

  def __init__(self):
   self.todaydetail = datetime.datetime.today() 
   global rlock

  def execute(self, sender, earg):
    try:
      with rlock:
        print("shoot_self", self)
        print("shoot_sender",sender)
        print("shoot_earg",earg)
#        self.todaydetail = datetime.datetime.today().strftime("%Y%m%d_%H%M%S")
        self.todaydetail = earg
        self.todaydetail = self.todaydetail +  "_" + threading.currentThread().getName()
        print("call by " + threading.currentThread().getName())
        print self.todaydetail
        os.system('raspistill -o ' + self.todaydetail + '.jpg -vf -hf -w 1024 -h 768 -t 1000 -ex antishake')
        time.sleep(1)
    except:
      print("cancel capture")
