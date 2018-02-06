from pylint import epylint as lint

#compile code in the repo and collect the compilation messages in the communication object
def to_compile(communication):
    (pylint_stdout, pylint_stderr) = lint.py_run("/".join([communication.location, "src"]), return_std=True)
    communication.compiling_messages = pylint_stdout
