from pylint import epylint as lint


def to_compile(communication):
    (pylint_stdout, pylint_stderr) = lint.py_run("/".join([communication.location, "src"]), return_std=True)
    communication.compiling_messages = pylint_stdout
