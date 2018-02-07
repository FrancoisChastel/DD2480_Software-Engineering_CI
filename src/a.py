#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from communication import communication
from downloader import downloader
from compilation import compilation
from notification import notification


def test_notification_1():
    # contract : get_message enable to return COMPILING_FAILED when parameter contains nothing
    c = communication.Result()
    c.state = 0
    m = notification.get_message(c)
    assert m
    
if __name__ == "__main__":
    test_notification_1()
