from ..pgscript import PgScript
from ..pgpigeon import PgPigeon


def create_scripts(commands, arguments):
    try:
        print(
            f":: Init command : sub-commands : {commands} , arguments : {arguments}")
        command_str = ""
        if len(commands) > 0:
            command_str = commands.pop(0)
        print(f":: Command : {command_str}.")
        arguments = [c for c in commands if c.__contains__('--')]
        pg_script = PgScript()
        pg_script.create_scripts()
        if command_str:
            method = globals()['get_command'](command_str)
            globals()[method](commands, arguments)
    except Exception as e:
        print(f":: Error : {e}")
