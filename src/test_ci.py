#!/usr/bin/env python
# -*- coding: utf-8 -*-


def test_compilation_1():
    #contract: to_compile enable to throw a AttributeError when parameter contains nothing
    c = communication.Result()
    with pytest.raises(AttributeError):
        compilation.to_compile(c)


def test_notification_1():
    assert 3 == 3
