import time
import Adafruit_BBIO.GPIO as GPIO

INTAVAL = 3
SLEEPTIME = 1
SENSOR_PIN = "P8_19"

GPIO.cleanup()
#GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

st = time.time()-INTAVAL

while True:
        print GPIO.input(SENSOR_PIN)
	#       if (GPIO.input(SENSOR_PIN)  and (st + INTAVAL < time.time())):
	#               st = time.time()
	#               print ("sensored")

	        time.sleep(SLEEPTIME)
