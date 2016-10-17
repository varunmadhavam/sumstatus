import urllib2
import time
import xml.etree.ElementTree as ET
import smtplib
url = "http://ip:1128/slp/sumabap/SID/monitor"
smsurl1='url'
smsurl2='url'
counter=0
check=2
interval=1800
sender = 'sum@nd1upgrade'
receivers = ['u@c','u@c']
message = """From: SUM SID <sum@sidupgrade>
To: x y <u@c>,m  n <m@n>
MIME-Version: 1.0
Content-type: text/html
Subject: SUM Running on SID requires your attention

<h1>SUM on SID Waiting For Dialog Input</h1>
"""
def sentmail():
	smtpObj = smtplib.SMTP('1.1.1.1',25)
	smtpObj.sendmail(sender, receivers, message)
	print "mail sent"
	return;
def sentsms():
	reqsms1 = urllib2.Request(smsurl1)
	reqsms2 = urllib2.Request(smsurl2)
	urllib2.urlopen(reqsms1)	
	urllib2.urlopen(reqsms2)	
	print "sms sent"
	return;
req = urllib2.Request(url)
req.add_header('Authorization', 'Basic xxxwfwfewefwefwfwef')
while True:
	response = urllib2.urlopen(req)
	output = response.read()
	root = ET.fromstring(output)
	status=root[0][4].text
	print status
	if (status == "slp.task.state.ERROR") or (status == "slp.task.state.DIALOG"):
		print "Process in dialog state"
		counter=counter+1
		if(counter==check):
			counter=0
			sentmail()
			sentsms()
	else:
		print "Process in non dialog state"
		if(counter>0):
			counter=counter-1
	time.sleep(interval)
