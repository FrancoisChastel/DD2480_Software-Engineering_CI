import email.message as e
import smtplib

#function to send email notification containing results of compilation and testing
def send_notifications(message):
	fromaddr = 'DD2480.CI@gmail.com'  # from addr
	toaddrs = 'DD2480.CI@gmail.com'  # to addr

	m = e.Message()  # setting up message to send
	m['From'] = "DD2480.CI@gmail.com"
	m['To'] = "DD2480.CI@gmail.com"
	m['Subject'] = "Compilation and Test results"
	m.set_payload(message)

	username = 'DD2480.CI@gmail.com'  # log into smtp
	password = 'DD2480CI'
	server = smtplib.SMTP('smtp.gmail.com:587')  # init smtp server
	server.ehlo()
	server.starttls()
	server.login(username, password)
	server.sendmail(fromaddr, toaddrs, m.as_string())
	server.quit()


if __name__ == "__main__":
	send_notifications(
		"Hello World!" + "\n" + "Test 1 success" + "\n" + "Test 2 Success")  # current test, should send an email to DD2480.CI@gmail.com with subject "Test Results" and message "Hello World!"
