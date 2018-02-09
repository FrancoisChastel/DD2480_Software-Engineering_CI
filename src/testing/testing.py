#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

import communication
import pytest
from cStringIO import StringIO


def to_test(result):
    """
    Launch the src/test_ci.py at the given location inside the communication object
    :param result: communication-object (see communication.py) that can hold all the information about the process
    :return: if the test has been launched or not
    """
    if result.state != communication.State.COMPILING_FAILED:
        args = "/".join([result.location, "src", "test_ci.py"])
        save_stdout = sys.stdout
        sys.stdout = test_result_buff = StringIO()

        pytest.main(args=str(args))
        sys.stdout = save_stdout

        test_result = test_result_buff.getvalue()
        test_result_buff.close()

        if "error" in test_result:
            result.state = communication.State.TEST_FAILED
        elif "warning" in test_result:
            result.state = communication.State.TEST_WARNED
        else:
            result.state = communication.State.TEST_SUCCEED

        result.test_messages = test_result
        return True
    else:
        return False
