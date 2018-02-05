from enum import Enum


class Result:
    __slot__ = ["state",
                "compiling_messages",
                "test_messages",
                "location",
                "commit",
                "author",
                "url_repo"]

    def __init__(self):
        pass


class State(Enum):
    COMPILING_FAILED = 0
    COMPILING_SUCCEED = 1
    COMPILING_WARNED = 2
    TEST_FAILED = 3
    TEST_SUCCEED = 4
    TEST_WARNED = 5