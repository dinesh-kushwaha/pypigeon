from ..constants import PIGEON_JSON, PG_PIGEON_SAMPLE_LISTNER_CODE


def configure(commands, arguments):
    print(
        f":: Init command : sub-commands : {commands} , arguments : {arguments}")
    command_str = ""
    if len(commands) > 0:
        command_str = commands.pop(0)
    print(f":: Command : {command_str}.")
    with open('pigeon.json', 'w') as f:
        f.write(PIGEON_JSON)
    if command_str:
        arguments = [c for c in commands if c.__contains__('--')]
        method = globals()['get_command'](command_str)
        globals()[method](commands, arguments)
