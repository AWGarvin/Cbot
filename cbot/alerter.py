from __future__ import print_function
import smtplib
import urllib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
'''email and text sender'''
'''Paden Stewart'''
'''User:craigslistpythonproject@gmail.com'''
'''Pass:Programmingisfun1'''

def alerter(item, recipient, phone_num = None, carrier = None):
	sender = "craigslistpythonproject@gmail.com"	
	if phone_num:
		phone_num = str(phone_num)
		if carrier == "Verizon":
			cellphone = phone_num + "@vtext.com"
		if carrier == "Sprint":
			cellphone = phone_num + "@messaging.sprintpcs.com"
		if carrier == "AT&T":
			cellphone = phone_num + "@txt.att.net"
		if carrier == "T-Mobile":
			cellphone = phone_num + "@tmomail.net"
		if carrier == "Virgin Mobile":
			cellphone = phone_num + "@vmobl.com"
		if carrier == "Nextel":
			cellphone = phone_num + "@messaging.nextel.com"
		if carrier == "Alltel":
			cellphone = phone_num + "@message.alltell.com"

		#format multipart message
		message = MIMEMultipart('related')
		message['From'] = sender
		message['To'] = recipient
		message['Subject'] = "Craigslist Item: " + item.title

		#format multipart textmessage
		textmessage = MIMEMultipart('related')
		textmessage['From'] = sender
		textmessage['To'] = recipient
		textmessage['Subject'] = ""

 		#text for email message
		altmessage = MIMEMultipart('alternative')
		message.attach(altmessage)
		body = 'Hello, <br> The item: ' + item.title + ' was posted: ' + item.date + '<br><img src = "cid:image1"><br>' + item.descr + '<br> Contact information: <br>' + item.email + '<br>' + item.phone
		altmessage.attach(MIMEText(body, 'html'))

		#text message text
		if phone_num:
			textbody = "An e-mail has been sent to you regarding your craigslist search of: " + item.title
			textmessage.attach(MIMEText(textbody, 'plain'))
		
		for pic in item.pics:
			#open, save and close image
			urllib.urlretrieve(pic, "test.jpg")
			img = open('test.jpg', 'rb')
			messageimage = MIMEImage(img.read())
			img.close()

			#attach image to message
			messageimage.add_header('Content-ID', '<image1>')
			message.attach(messageimage)
		
		#conect to server and send email and text
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(sender, "Programmingisfun1")
		server.sendmail(sender, recipient, message.as_string())
		if phone_num:
			server.sendmail(sender, cellphone, textmessage.as_string())
		server.quit() 

#test class and test main
'''
class Item():
    def __init__(self):
        # lines followed by hash will be needed for email
        # self.region = None
        # self.category = None #
        # self.searchterm = None #
        self.title = "Test Item" #
        self.descr = "It's some real good stuff" #
        self.price = "$1,000,000" #
        self.email = "mybean@gmail.com" #
        self.phone = "420420420" #
        self.date = "April 20th 2420" #
        # need to also send carrier
        # need link to listing
        # post id number possibly


if __name__ == "__main__":
	imgurl = "https://41.media.tumblr.com/f608ad44a7f1ebfe473912a2d13556a4/tumblr_np8f3uJWSb1t5auluo1_1280.jpg"
	item1 = Item()
	recipient = "craigslistpythonproject@gmail.com"
	phone_num = "7179915983"
	carrier = "Verizon"
	alerter(item1, recipient, imgurl, phone_num, carrier)

'''







