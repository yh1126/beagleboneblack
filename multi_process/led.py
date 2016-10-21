import RPi.GPIO as GPIO
import time

class Led(object):
  def __init__(self):
    self.PIN = 21

  def execute(self, sender, earg):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.PIN, GPIO.OUT)
    GPIO.output(self.PIN, GPIO.HIGH)
    time.sleep(10)
    GPIO.cleanup()
