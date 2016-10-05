#!/usr/local/bin/python
# -*- coding: utf-8 -*-
###/usr/bin/python
# shoot.py

import os
import time
import datetime

class Shoot(object):

  def __init__(self):
   selft.todaydetail = datetime.datetime.today() 

  def execute(self, earg):
    self.todaydetail = datetime.datetime.today().strftime("%Y%m%d_%H%M%S")
    print self.todaydetail
    os.system('raspistill -o ' + self.todaydetail + '.jpg -vf -hf -w 1024 -h 768 -t 1000 -ex antishake')
    time.sleep(2)
