import sys

import pytest

import communication
from compilation import compilation


#contract: test for compilation errors using state value where 0 is error, 1 is no error, and 2 is compilation warning
def test_compilation_1():
    c = communication.Result()
    compilation.to_compile(c)
    assert c.state != 0, "Compilation failed"  # where is state updated?
    if c.state == 2:
        print("Compilation warning!")
    print(c.compiling_messages)

#contract: test for attribute errors during compilation process
def test_compilation_2():  # needs an assert statement
    commun = communication.Result()
    with pytest.raises(AttributeError):
        compilation.to_compile(commun)

#contract: test that notifications are correctly sent via email with the correct compilation and testing results
def test_notification_1():
    assert 3 == 3


def test_all(path):
    saveout = sys.stdout
    tout = open(path, 'w')
    sys.stdout = tout

    args = ['testing/testing.py']
    pytest.main(args)

    sys.stdout = saveout
    tout.close()
