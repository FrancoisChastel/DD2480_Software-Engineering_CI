#!/usr/bin/env python
# -*- coding: utf-8 -*-
from enum import Enum

#object holding information so that different features can easily communicate with one another

class Result:
    """
    Communication object that allow all the packages to communicate with each other
    """
    __slot__ = ["state",
                "compiling_messages",
                "test_messages",
                "location",
                "commit",
                "author",
                "owner",
                "url_repo",
                "repository"]

    def __init__(self):
        pass


class State(Enum):
    COMPILING_FAILED = 0
    COMPILING_SUCCEED = 1
    COMPILING_WARNED = 2
    TEST_FAILED = 3
    TEST_SUCCEED = 4
    TEST_WARNED = 5
