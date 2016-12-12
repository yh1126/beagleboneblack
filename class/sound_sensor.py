#!/usr/bin/env python
# -*- coding: utf-8 -*-
# SEN02281P ----- RaspberryPi GPIO
# =SIG ---------- 13
# =NC
# =VCC ---------- 2
# =GND ---------- 20

import paho.mqtt.client as mqtt
import time
import RPi.GPIO as GPIO

def on_connect(client,userdata,flags,rc):
  print( "Connection with result code " + str(rc) )
  client.subscribe( "sen02281p" )

def on_message(client,userdata,msg):
  print( msg.topic + " " + str(msg.payload) )

def reading(sensor):
  sum = -1 
  if sensor == 0:
    sum = 0
    for i in range(0,20):
      time.sleep(0.1)
      a = GPIO.input(SIG)
      sum += a
  else:
    print "Incorrect function."

  return sum

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
SIG = 13
GPIO.setup(SIG,GPIO.IN)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect( "iot.eclipse.org", 1883 )
while client.loop() == 0:
  msg = reading(0);
  client.publish( "sen02281p", msg, 0, True )
  pass

GPIO.cleanup()
