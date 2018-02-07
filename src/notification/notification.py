import email.message as e
import smtplib
# !/usr/bin/env python
# -*- coding: utf-8 -*-
import configs

import communication


def send_notifications(result):
    message = get_message(result)

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


def get_message(result):
    message = ""

    if result.state == communication.State.COMPILING_FAILED:
        message = configs.ER_CPL_MESSAGE % (result.state,
                                            result.author,
                                            result.commit,
                                            result.url_repo,
                                            result.compiling_messages)
    elif result.state == communication.State.TEST_FAILED:
        message = configs.ER_TST_MESSAGE % (result.state,
                                            result.author,
                                            result.commit,
                                            result.url_repo,
                                            result.test_messages)
    elif result.state == communication.State.TEST_SUCCEED:
        message = configs.SCC_MESSAGE % (result.state,
                                         result.author,
                                         result.commit,
                                         result.url_repo)
    elif result.state == communication.State.TEST_WARNED:
        message = configs.WRN_CPL_MESSAGE % (result.state,
                                             result.author,
                                             result.commit,
                                             result.url_repo,
                                             result.compiling_messages, result.test_messages)

    return message
