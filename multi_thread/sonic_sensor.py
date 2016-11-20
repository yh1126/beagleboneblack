import RPi.GPIO as GPIO
import time
import event

class SonicSensor(object):

  def __init__(self):
    self.TRIG = 21
    self.ECHO = 20
    self.pulse_start = 0
    self.pulse_end = 0
    self.pulse_duration = 0
    self.distance = 0
    self.evt = self.Event()
  
  def measure(self, sender, earg):
    while True:
      try:
        GPIO.setmode(GPIO.BCM) #GPIO.BCM: GPIO number , GPIO.BOARD:PIN number 
        print "Distance Measurement in Progress"
        GPIO.setup(self.ECHO, GPIO.IN)
        GPIO.setup(self.TRIG, GPIO.OUT)
        GPIO.output(self.TRIG, GPIO.HIGH)
        time.sleep(0.00001) #10us = sonic sensor trig signal
        GPIO.output(self.TRIG, GPIO.LOW)
        
        while GPIO.input(self.ECHO)==0:
          self.pulse_start = time.time()
        
        while GPIO.input(self.ECHO)==1:
          self.pulse_end = time.time()
        
        self.pulse_duration = self.pulse_end - self.pulse_start
        
        self.distance = self.pulse_duration * 17150
        self.distance = round(self.distance, 2)
        print "Distance: ", self.distance , "cm"
        if(self.distance < 20):
          print("call capture method")
          self.evt()
        else:
          print("not call capture method")
        time.sleep(0.3)

      except:
        print("break sensor")
        break
  
    GPIO.cleanup()
