#!/usr/bin/env python
# -*- coding: utf-8 -*-
import communication
from pylint import epylint as lint


def to_compile(result):
    (pylint_stdout, pylint_stderr) = lint.py_run("/".join([result.location, "src"]), return_std=True)

    result.compiling_messages = pylint_stdout.buf

    if "error" in result.compiling_messages:
        result.state = communication.State.COMPILING_FAILED
    elif "warning" in result.compiling_messages:
        result.state = communication.State.COMPILING_WARNED
    else:
        result.state = communication.State.COMPILING_SUCCEED
