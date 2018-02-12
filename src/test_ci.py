#!/usr/bin/env python
# -*- coding: utf-8 -*-
import communication
import pytest
import urllib2
import imaplib
import email
from compilation import compilation
from downloader import downloader
from notification import notification


def test_downloader_1():
    # contract : download_commit enable to throw a ValueError when parameter is empty
    c = communication.Result()
    with pytest.raises(ValueError):  # assert when not get a ValueError
        downloader.download_commit(c)


def test_downloader_2():
    # contract : download_commit enable to throw an HTTPError when parameters are nonsense
    c = communication.Result()
    c.url_repo = "https://www.github.com"
    c.owner = "shenmemingzi"
    c.repository = "NotHaveThisRepo"
    c.commit = "112a08f18ff4bee27db39fd857ffe910a3934a4c"
    with pytest.raises(urllib2.HTTPError):  # assert when not get an HTTPError
        downloader.download_commit(c)


def test_compilation_1():
    # contract : to_compile enable to throw a ValueError when parameter contains nothing
    c = communication.Result()
    with pytest.raises(ValueError):  # assert when not get a ValueError
        compilation.to_compile(c)


def test_compilation_2():
    # contract : to_compile enable to throw an IOError when the location is wrong
    c = communication.Result()
    c.location = "nowhere"
    with pytest.raises(IOError):  # assert when not get an IOError
        compilation.to_compile(c)


def test_compilation_3():
    #contract : check that compilation state is not FAILED
    c = communication.Result()
    assert c.state != communication.State.COMPILING_FAILED

def test_compilation_4():
    #contract : check that compilation has not failed, and notify if warning
    c = communication.Result()
    c_state = c.state
    assert c_state != communication.State.COMPILING_FAILED
    if c_state == communication.State.COMPILING_WARNED:
        print("Compilation Warning!")    

def test_notification_1():
    # contract : get_message enable to throw a ValueError when parameter contains nothing
    c = communication.Result()
    with pytest.raises(ValueError):  # assert when not get a ValueError
        notification.get_message(c)


def test_notification_2():
    # contract : get_message enable to return nothing when result state is 0, which is COMPILING_FAILED
    c = communication.Result()
    c.state = 0
    m = notification.get_message(c)
    expected = "Error triggered while compiling with error code : 0\n\t* Commit author : \n\t* Commit id     : " \
               "\n\t* Source url    : \n==================================================================" \
               "\n\t* Compiler logs : \n\n"
    assert m == expected


def test_notification_3():
    # contract : get_message enable to raise a ValueError when result state is a garbage value
    c = communication.Result()
    c.state = 10
    with pytest.raises(ValueError):  # assert when not get a ValueError
        m = notification.get_message(c)


def test_notification_4():
    # contract: email sent contains all fields set from result structure
    
    # populate result structure
    c = communication.Result()
    c.state = 0
    c.author = 'Brian'
    c.commit = 'test_commit_number'
    c.url_repo = 'www.test.com'
    c.compiling_messages = 'fail'

    #send email
    notification.send_notifications(c)

    #Login to email server
    username = 'DD2480.CI@gmail.com'
    password = 'DD2480CI'
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(username, password)
    mail.select('inbox')

    #select mailbox
    type, data = mail.search(None, 'ALL')
    mail_ids = data[0]

    #select email
    id_list = mail_ids.split()
    latest_email_id = int(id_list[-1])

    #check for all fields
    typ, data = mail.fetch(latest_email_id, '(RFC822)')
    if isinstance(data[0], tuple):

        resp = data[0][1]
        msg = email.message_from_string(resp)
        msg = str(msg)
        assert msg.find('Brian') != -1 and msg.find('test_commit_number') != -1 and msg.find('www.test.com') != -1 and \
              msg.find('fail') != -1 and msg.find('0') != -1
