import sys


def get_command(command_string):
    return command_string.replace('-', "_")

def next_sys_args(args):
    command = args[0]
    sys.argv = args.pop(0)
    return command

def get_command_args(args):
    command_args = [arg for arg in args if arg.__contains__(f"--")]
    return command_args


def get_args_as_dict(args):
    args = get_command_args(args)
    arg_dict = {}
    for arg in args:
        arg_str = arg[2:]
        _args = arg_str.split("=")
        if len(_args) <= 2:
            arg_dict[_args[0]] = _args[1]
    return arg_dict
