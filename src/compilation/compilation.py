from pylint import epylint as lint


def to_compile(location):
    (pylint_stdout, pylint_stderr) = lint.py_run("/".join([location, "src"]), return_std=True)

    return pylint_stdout
