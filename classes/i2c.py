#!/usr/bin/python
# -*- coding: utf-8 -*-
  
import smbus
import time
  
i2c = smbus.SMBus(1)
address = 0x48 #アドレス指定
  
while True:
    block = i2c.read_i2c_block_data(address, 0x00, 12) #データの取得
    temp = (block[0] << 8 | block[1]) >> 3
    if(temp >= 4096):
        temp -= 8192
    print("Temperature:%6.2f" % (temp / 16.0))
    time.sleep(1)
