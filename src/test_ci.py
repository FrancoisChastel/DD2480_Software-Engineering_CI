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
    # contract : download_commit enable to throw an AttributeError when parameter contains nothing
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
    # contract : get_message enable to return nothing when r.state equals something else
    c = communication.Result()
    c.state = 0
    m = notification.get_message(c)
    assert not m

    c.state = 10
    m = notification.get_message(c)
    assert not m

def test_notification_3():
    # contract : get_message enable to throw an AttributeError when r.state is right while other param. are null
    c = communication.Result()
    c.state = communication.State.TEST_SUCCEED
    with pytest.raises(AttributeError): #assert when not get an AttributeError
        m = notification.get_message(c)

@pytest.mark.parametrize("commit",[
    ("111222"),
    ("222333")
    ])
def test_notification_4(commit):        #paramter is the commit number from the communication structure,
                                        #exactly as it was passed into the send_notification function
    # contract : 
    #Login to email server
    username = 'DD2480.CI@gmail.com'    
    password = 'DD2480CI'
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(username,password)
    mail.select('inbox')

    #select mailbox
    type, data = mail.search(None,'ALL')
    mail_ids = data[0]

    #select email
    id_list = mail_ids.split()   
    first_email_id = int(id_list[0])
    latest_email_id = int(id_list[-1])

    #cycle to find correct email
    for i in range(latest_email_id,first_email_id, -1):
        typ, data = mail.fetch(i, '(RFC822)' )

        for response_part in data:
            if isinstance(response_part, tuple):
                msg = email.message_from_string(response_part[1])
                email_subject = msg['subject']
                if commit not in email_subject:
                    pass
                else:
                    assert "Commit " + commit + "results"  == email_subject     #asserting the subjuct contains the proper commit number
