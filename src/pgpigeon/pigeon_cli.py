import sys
from .pgpigeon import PgPigeon
# Modules import is required don't remove it.
from .modules import *


def startup():
    try:
        for arg in sys.argv:
            print(f":: arg v : {arg}")
        cli = sys.argv.pop(0)
        print(f":: {cli.upper()} CLI is running the command.")
        command_str = ""
        if len(sys.argv) > 0:
            command_str = sys.argv.pop(0)
        arguments = [c for c in sys.argv if c.__contains__('--')]
        if command_str:
            # configure-trigger will be converted to configure_trigger
            method = globals()['get_command'](command_str)
            if not globals().__contains__(method):
                print(f":: Invalid pigeon command")
                return
            globals()[method](sys.argv, arguments)
    except Exception as e:
        raise Exception(f":: Invalid command.")
