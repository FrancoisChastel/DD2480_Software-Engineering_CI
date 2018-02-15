#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import communication
from pylint import epylint as lint


def to_compile(result):
    """
    Execute a static analysis of the code at the given location given by result object at the directory /src
    :param result: communication-object (see communication.py) that can hold all the information about the process
    :return: N/A
    """
    if result.location == "":
        raise ValueError("Non-valid location for compiling")

    path = "/".join([result.location, "src"])
    print(path)
    (pylint_stdout, pylint_stderr) = lint.py_run(path, return_std=True)

    result.compiling_messages = pylint_stdout.buf

    if ": error" in result.compiling_messages:
        result.state = communication.State.COMPILING_FAILED
    elif ": warning" in result.compiling_messages:
        result.state = communication.State.COMPILING_WARNED
    else:
        result.state = communication.State.COMPILING_SUCCEED
