from twilio.rest import TwilioRestClient 
import RPi.GPIO as GPIO
import datetime
import time
from email.Utils import formatdate, parsedate
from buzz import buzz
from secret import MY_AUTH_TOKEN, MY_ACCOUNT_SID, MY_DIGITS

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)

THIS_NUMBER = +17177734070
ACCOUNT_SID =MY_ACCOUNT_SID
AUTH_TOKEN = MY_AUTH_TOKEN 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 

while(True):
	current_time = time.mktime(time.localtime())
	recent=current_time-1
	messages = client.sms.messages.list(To=THIS_NUMBER)[0:2]
	for message in messages:
		while message.date_sent==None:
			time.sleep(1)
		date_sent=time.mktime(parsedate(message.date_sent))
		if recent<=date_sent:
			if message.from_ == MY_DIGITS:
				if message.body == "open":
					buzz() 
