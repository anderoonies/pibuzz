# Python core
import datetime
import time

# Raspberry Pi
import RPi.GPIO as GPIO

# Twilio
from twilio.rest import TwilioRestClient

# Time utilities
from email.Utils import formatdate, parsedate

# User-defined
from secret import AUTH_TOKEN, ACCOUNT_SID, PHONE_NUMBER

# Constants
THIS_NUMBER = +17177734070

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

def initialize_rpi():
    """Sets up Raspberry Pi for input/output.
    """
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(26, GPIO.OUT)

def initialize_client():
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

def buzz():
    """Buzz me in! Activates GPIO pin"""
    GPIO.output(26, 1)
    time.sleep(1)
    GPIO.output(26, 0)

def is_valid(message):
    """Check if a message is valid"""
    date_sent = time.mktime(parsedate(message.date_sent))
    current_time = time.mktime(time.localtime())
    recent_time = current_time - 1

    return ((recent_time <= date_sent) and
             message.from_ == PHONE_NUMBER)

def listen():
    while(True):
        message = client.sms.messages.list(To=THIS_NUMBER)[0]
        if is_valid(message):
            if message.body == "open":
                buzz()

if __name__ == '__main__':
    initialize_rpi()
    initialize_client()
    listen()
