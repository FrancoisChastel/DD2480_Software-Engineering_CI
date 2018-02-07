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

def test_notification_4():
    # contract : get_message enable to throw an AttributeError when r.state is right while other param. are null
    c = communication.Result()
    c.state = communication.State.TEST_SUCCEED
    with pytest.raises(AttributeError): #assert when not get an AttributeError
        m = notification.get_message(c)


