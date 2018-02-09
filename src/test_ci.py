#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import urllib2
import imaplib
import email
from communication import communication
from downloader import downloader
from compilation import compilation
from notification import notification

def test_downloader_1():
    # contract : download_commit enable to throw an AttributeError when parameter is empty
    c = communication.Result()
    with pytest.raises(AttributeError): #assert when not get an AttributeError
        downloader.download_commit(c)

    c.url_repo = "https://www.github.com"
    with pytest.raises(AttributeError): #assert when not get an AttributeError
        downloader.download_commit(c)

def test_downloader_2():
    # contract : download_commit enable to throw an HTTPError when parameters are nonsense
    c = communication.Result()
    c.url_repo = "https://www.github.com"
    c.owner = "shenmemingzi"
    c.repository = "NotHaveThisRepo"
    c.commit = "112a08f18ff4bee27db39fd857ffe910a3934a4c"
    with pytest.raises(urllib2.HTTPError): #assert when not get an HTTPError
        downloader.download_commit(c)

def test_compilation_1():
    # contract : to_compile enable to throw an AttributeError when parameter contains nothing
    c = communication.Result()
    with pytest.raises(AttributeError): #assert when not get an AttributeError
        compilation.to_compile(c)

def test_notification_1():
    # contract : get_message enable to throw an AttributeError when parameter contains nothing
    c = communication.Result()
    with pytest.raises(AttributeError): #assert when not get an AttributeError
        m = notification.get_message(c)

def test_notification_2():
    # contract : get_message enable to return nothing when result state is 0, which is COMPILING_FAILED
    c = communication.Result()
    c.state = 0
    m = notification.get_message(c)
    assert not m
    
def test_notification_3(): 
    # contract : get_message enable to return nothing when result state is a garbage value
    c = communication.Result()
    c.state = 10
    m = notification.get_message(c)
    assert not m

# TO FIX

# def test_notification_4():
    # contract : get_message enable to throw an AttributeError when r.state is right while other param. are null
#    c = communication.Result()
#    c.state = communication.State.TEST_SUCCEED
#    with pytest.raises(AttributeError): #assert when not get an AttributeError
#        m = notification.get_message(c)


#TO FIX
#WORKS WHEN RUN ALONE, BUT NOT WHEN RUNNING WITH PYTEST

# def test_notification_5():
#     # contract: email sent contains all fields set from result structure

#     #populate result structure
#     c = communication.Result()
#     c.state = communication.State.COMPILING_FAILED
#     c.author = 'Brian'
#     c.commit = 'test_commit_number'
#     c.url_repo = 'www.test.com'
#     c.compiling_messages = 'fail'

#     #send email
#     notification.send_notifications(c)

#     #Login to email server
#     username = 'DD2480.CI@gmail.com'    
#     password = 'DD2480CI'
#     mail = imaplib.IMAP4_SSL("imap.gmail.com")
#     mail.login(username,password)
#     mail.select('inbox')

#     #select mailbox
#     type, data = mail.search(None,'ALL')
#     mail_ids = data[0]

#     #select email
#     id_list = mail_ids.split()   
#     latest_email_id = int(id_list[-1])

#     #check for all fields
#     typ, data = mail.fetch(latest_email_id, '(RFC822)' )
#     if isinstance(data[0], tuple):
#         resp = data[0][1]
#         msg = email.message_from_string(resp)
#         msg = str(msg)
#         assert msg.find('Brian') != -1 and msg.find('test_commit_number') != -1 and msg.find('www.test.com') != -1 and \
#         msg.find('fail') != -1 and msg.find('COMPILING_FAILED') != -1
