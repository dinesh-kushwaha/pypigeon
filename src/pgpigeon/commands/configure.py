from ..constants import BASE_PIGEON_FOLDER, PIGEON_JSON, PG_PIGEON_SAMPLE_LISTENER_CODE, PIGEON_JSON_FILE
import os


def configure(commands, arguments):
    command_str = ""
    if len(commands) > 0:
        command_str = commands.pop(0)

    pigeon_json_file = PIGEON_JSON_FILE
    cwd = os.getcwd()
    pigeon_json_dir = os.path.join(cwd, BASE_PIGEON_FOLDER)
    if not os.path.exists(pigeon_json_dir):
        os.mkdir(pigeon_json_dir)

    pigeon_json_file = os.path.join(cwd, BASE_PIGEON_FOLDER, PIGEON_JSON_FILE)
    with open(pigeon_json_file, 'w') as f:
        f.write(PIGEON_JSON)
    print(f":: Pigeon has been configured successfully")
    print(
        f":: Pigeon configuration file '{pigeon_json_file}' has been created successfully at location {pigeon_json_file}")
    if command_str:
        arguments = [c for c in commands if c.__contains__('--')]
        method = globals()['get_command'](command_str)
        globals()[method](commands, arguments)
