from twilio.rest import TwilioRestClient 
import datetime
import time
from email.Utils import formatdate
from buzz import buzz

 
# put your own credentials here 
ACCOUNT_SID = "AC9851b14cefed4d261e5819345e65db72" 
AUTH_TOKEN = "7aa9111cda6210188dd5b85033eb4f96" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 

while(True):
	dt = datetime.datetime.now() + datetime.timedelta(seconds=-4)
	formatTime=formatdate(float(dt.strftime('%s')))
	messages = client.messages.list()[0:2]
	for message in messages:
		if formatTime<=message.date_sent:
			if message.from_ == "+17176026004":
				if message.body == "open":
					buzz() 
