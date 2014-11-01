from twilio.rest import TwilioRestClient 
import datetime
import time
from email.Utils import formatdate
from buzz import buzz
from secret import MY_AUTH_TOKEN, MY_ACCOUNT_SID, MY_DIGITS

ACCOUNT_SID =MY_ACCOUNT_SID
AUTH_TOKEN = MY_AUTH_TOKEN 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 

while(True):
	dt = datetime.datetime.now() + datetime.timedelta(seconds=-4)
	formatTime=formatdate(float(dt.strftime('%s')))
	messages = client.messages.list()[0:2]
	for message in messages:
		if formatTime<=message.date_sent:
			if message.from_ == MY_DIGITS:
				if message.body == "open":
					buzz() 
