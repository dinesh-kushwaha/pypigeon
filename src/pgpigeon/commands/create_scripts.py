from ..common import PgCommon
from ..pgscript import PgScript


def create_scripts(commands, arguments):
    try:
        pg_common = PgCommon()
        if not pg_common.is_pigeon_config_available():
            print(
                f":: Pigeon config is not available.\n Run command [ pigeon configure ] to create config")
            return
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
            if not globals().__contains__(method):
                print(f":: Invalid pigeon command")
                return
            globals()[method](commands, arguments)
    except Exception as e:
        print(f":: Error : {e}")
