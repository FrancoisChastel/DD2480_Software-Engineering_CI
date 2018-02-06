import sys

import pytest

import communication
from compilation import compilation


def test_downloader_1():
    assert 1 == 1


def test_compilation_1():
    c = communication.Result()
    compilation.to_compile(c)
    assert c.state != 0, "Compilation failed"  # where is state updated?
    if c.state == 2:
        print("Compilation warning!")
    print(c.compiling_messages)


def test_compilation_2():  # needs an assert statement
    commun = communication.Result()
    with pytest.raises(AttributeError):
        compilation.to_compile(commun)


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
