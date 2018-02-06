import pytest
import sys

import communication
from downloader import downloader
from compilation import compilation
from notification import notification

def test_downloader():
    assert 1 == 1 

def test_compilation():
    commun = communication.Result()
    with pytest.raises(AttributeError):
        compilation.to_compile(commun)

def test_notification():
    assert 3 == 3

def TestAll(path):
    saveout = sys.stdout
    tout = open(path, 'w')
    sys.stdout = tout

    args = ['testing/testing.py']
    pytest.main(args)

    sys.stdout = saveout
    tout.close()
