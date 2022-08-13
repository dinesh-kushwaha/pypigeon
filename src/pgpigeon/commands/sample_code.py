from ..pgpigeon import PgPigeon
from ..constants import PIGEON_JSON, PG_PIGEON_SAMPLE_LISTNER_CODE


def sample_code(commands, arguments):
    try:
        print(
            f":: Init command : sub-commands : {commands} , arguments : {arguments}")
        command_str = ""
        if len(commands) > 0:
            command_str = commands.pop(0)
        print(f":: Command : {command_str}.")
        arguments = [c for c in commands if c.__contains__('--')]
        with open('pigeon.py', 'w') as f:
            f.write(PG_PIGEON_SAMPLE_LISTNER_CODE)
        if command_str:
            method = globals()['get_command'](command_str)
            globals()[method](commands, arguments)
    except Exception as e:
        print(f":: Error : {e}")
