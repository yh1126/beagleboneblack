import threading
import RPi.GPIO as GPIO
import time
import event
import datetime

class SonicSensorPeriodci(object):
    def __init__(self):
        self.evt = event.Event()
        self.TRIG = 21
        self.ECHO = 20
        self.pulse_start = 0
        self.pulse_end = 0
        self.pulse_duration = 0
        self.distance = 0

    def main(self):
        while True:
            try:
                GPIO.setmode(GPIO.BCM)
                print("Distance Measurement in Progress")
                GPIO.setup(self.ECHO, GPIO.IN)
                GPIO.setup(self.TRIG, GPIO.OUT)
                GPIO.output(self.TRIG, GPIO.HIGH)
                time.sleep(0.00001)
                GPIO.output(self.TRIG, GPIO.LOW)

                while GPIO.input(self.ECHO)==0:
                    self.pulse_start = time.time()

                while GPIO.input(self.ECHO)==1:
                    self.pulse_end = time.time()

                self.pulse_duration = self.pulse_end - self.pulse_start

                self.distance = self.pulse_duration * 17150
                self.distance = round(self.distance, 2)
                print("Distance: ", self.distance , "cm")
                if(self.distance < 20):
                    self.user_method2()
                else:
                    pass

                time.sleep(0.5)

                self.user_method1()

          except:
              self.exception_method()

    def user_method1(self, earg=None):
         print('call user method')

    def user_method2(self, earg=None):
         print('hello, world')

    def exception_method(self):
        GPIO.cleanup(self.channel)
        GPIO.remove_event_detect(self.channel)
