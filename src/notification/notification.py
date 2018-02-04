import smtplib

def send_notifications(message):

	fromaddr = 'DD2480.CI@gmail.com'	#from addr
	toaddrs  = 'DD2480.CI@gmail.com'	#to addr
	msg = "\r\n".join([					#message with headers for from, to, and subject
	  "From: DD2480.CI@gmail.com",
	  "To: DD2480.CI@gmail.com",
	  "Subject: Test Results",
	  "",
	  message
	  ])
	username = 'DD2480.CI@gmail.com'	#log into smtp
	password = 'DD2480CI'
	server = smtplib.SMTP('smtp.gmail.com:587')	#init smtp server
	server.ehlo()
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, toaddrs, msg)
	server.quit()


if __name__ == "__main__":
	send_notifications("Hello World!")		#current test, should send an email to DD2480.CI@gmail.com with subject "Test Results" and message "Hello World!"


	