import email.message as e
import smtplib
# !/usr/bin/env python
# -*- coding: utf-8 -*-
import configs

import communication


def send_notifications(result):
    """
    Function that will send by e-mail a notification of the state of the testing and compiling process
    :param result: communication-object (see communication.py) that can hold all the information about the process
    :return: True once the mail sent
    """
    #Retrieving the response from system tests to send
    message = get_message(result)

    #can be changed: Email to send from and email to send to
    fromaddr = 'DD2480.CI@gmail.com'
    toaddrs = 'DD2480.CI@gmail.com'

    # setting up message fields
    m = e.Message()
    m['From'] = "DD2480.CI@gmail.com"
    m['To'] = "DD2480.CI@gmail.com"
    m['Subject'] = "Compilation and Test results"
    m.set_payload(message)

    #logging into smtp server and sending mail
    username = 'DD2480.CI@gmail.com'
    password = 'DD2480CI'
    server = smtplib.SMTP('smtp.gmail.com:587')         #log into smtp
    server.ehlo()                                       #setting up server communication
    server.starttls()                                   #start tls for secure connection
    server.login(username, password)                    #log into email account
    server.sendmail(fromaddr, toaddrs, m.as_string())   #sending email
    server.quit()

    return True


def get_message(result):
    """
    Function that allow you get a string that could be sent as notification with all the useful information
    :param result: communication-object (see communication.py) that can hold all the information about the process
    :return: a string holding the message that need to be sent
    """
    message = ""

    state = result.state

    if not isinstance(state, communication.State):
        if state in [0, 1, 2, 3, 4, 5]:
            state = communication.State(state)
        else:
            raise ValueError("The state {0} is not recognized".format(state))

    #check state of input to retrieve correct messages and information
    if state == communication.State.COMPILING_FAILED:  # failed compilation
        message = configs.ER_CPL_MESSAGE % (result.state,
                                            result.author,
                                            result.commit,
                                            result.url_repo,
                                            result.compiling_messages)
    elif state == communication.State.TEST_FAILED:  # failed test(s)
        message = configs.ER_TST_MESSAGE % (result.state,
                                            result.author,
                                            result.commit,
                                            result.url_repo,
                                            result.test_messages)
    elif state == communication.State.TEST_SUCCEED:  # passed all tests
        message = configs.SCC_MESSAGE % (result.state,
                                         result.author,
                                         result.commit,
                                         result.url_repo,
                                            result.test_messages)
    elif state == communication.State.TEST_WARNED:  # test(s) warning
        message = configs.WRN_CPL_MESSAGE % (result.state,
                                             result.author,
                                             result.commit,
                                             result.url_repo,
                                             result.compiling_messages, result.test_messages)
    else:
        raise ValueError("The state {0} is not managed by the notification system".format(state))
    return message
