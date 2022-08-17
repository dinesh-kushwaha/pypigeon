from ..common import PgCommon
from ..constants import BASE_PIGEON_FOLDER, PG_PIGEON_SAMPLE_CODE_FILE, PG_PIGEON_SAMPLE_LISTENER_CODE
import os


def sample_code(commands, arguments):
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
        sample_code_file = PG_PIGEON_SAMPLE_CODE_FILE
        cwd = os.getcwd()
        sample_code_dir = os.path.join(cwd, BASE_PIGEON_FOLDER)
        if not os.path.exists(sample_code_dir):
            os.mkdir(sample_code_dir)

        sample_code_file = os.path.join(
            cwd, BASE_PIGEON_FOLDER, PG_PIGEON_SAMPLE_CODE_FILE)
        with open(sample_code_file, 'w') as f:
            f.write(PG_PIGEON_SAMPLE_LISTENER_CODE)

        init_file = os.path.join(
            cwd, BASE_PIGEON_FOLDER, "__init__.py")
        with open(init_file, 'w') as f:
            f.write("")

        print(f":: Pigeon sample code has been generated successfully")
        print(
            f":: Pigeon configuration file '{PG_PIGEON_SAMPLE_CODE_FILE}' has been created successfully at location {sample_code_file}")
        if command_str:
            method = globals()['get_command'](command_str)
            if not globals().__contains__(method):
                print(f":: Invalid pigeon command")
                return
            globals()[method](commands, arguments)
    except Exception as e:
        print(f":: Error : {e}")
