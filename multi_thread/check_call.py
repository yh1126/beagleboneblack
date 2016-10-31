import RPi.GPIO as GPIO
import time
import sonic_sensor

class Led(object):
  def __init__(self):
    self.sonic = sonic_sensor.SonicSensor()

  def execute(self):
  #def execute(self):
    self.sonic.measure(self,  2)
   # GPIO.setmode(GPIO.BCM)
   # GPIO.setup(self.PIN, GPIO.OUT)
   # GPIO.output(self.PIN, GPIO.HIGH)
   # time.sleep(5)
   # GPIO.cleanu()

l = Led()
l.execute()
