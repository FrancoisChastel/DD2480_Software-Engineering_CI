#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from cStringIO import StringIO

import communication
import pytest


def to_test(result):
    if result.state != communication.State.COMPILING_FAILED:
        args = "/".join([result.location, "src", "test_ci.py"])
        save_stdout = sys.stdout
        sys.stdout = test_result_buff = StringIO()

        pytest.main(args=str(args))
        test_result_buff.close()
        sys.stdout = save_stdout

        test_result = test_result_buff.getvalue()

        if "error" in test_result:
            result.state = communication.State.TEST_FAILED
        elif "warning" in test_result:
            result.state = communication.State.TEST_WARNED
        else:
            result.state = communication.State.TEST_SUCCEED

        result.test_messages = test_result


    else:
        # Do not launch the test regarding the fact compiling failed
        pass
