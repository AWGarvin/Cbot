from __future__ import print_function
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
'''email sender'''
'''Paden Stewart'''
'''User:craigslistpythonproject@gmail.com'''
'''Pass:Programmingisfun1'''
if __name__ == "__main__":
    sender = "craigslistpythonproject@gmail.com"  #our email
    # reciever = "craigslistpythonproject@gmail.com"#recipients email
    # reciever = "alexwgarvin@gmail.com"
    reciever = "zmauer1@gmail.com"
    cellphone = "7179915983@vtext.com"#need to format according to carrier
    
    #format multipart message
    message = MIMEMultipart('related')
    message['From'] = sender
    message['To'] = reciever
    message['Subject'] = "Craigslist Item"

    #format multipart message
    textmessage = MIMEMultipart('related')
    textmessage['From'] = sender
    textmessage['To'] = reciever
    textmessage['Subject'] = ""

    #email message text
    altmessage = MIMEMultipart('alternative')
    message.attach(altmessage)
    body = '<b>Your <i>Item</i> has been found!</b><br><img src="cid:image1"><br> Look a pic!'
    altmessage.attach(MIMEText(body, 'html'))

    #text message text
    textbody = 'An e-mail has been sent to you regarding your craigslist search!'
    textmessage.attach(MIMEText(textbody, 'plain'))

    #open, save and close image
    fp = open('test.jpg', 'rb')
    messageimage = MIMEImage(fp.read())
    fp.close()

    #attach image to message
    messageimage.add_header('Content-ID', '<image1>')
    message.attach(messageimage)

    #connect to server and send email and text
    server = smtplib.SMTP('smtp.gmail.com', 587)#need to change according to mail service
    server.starttls()
    server.login(sender, "Programmingisfun1") 
    server.sendmail(sender, reciever, message.as_string())
    server.sendmail(sender, cellphone, textmessage.as_string())
    server.quit()



