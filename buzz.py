import RPi.GPIO as GPIO
import time

def buzz():
	print 'firing'
	GPIO.output(26, 1)
	time.sleep(2)
	GPIO.output(26, 0)
