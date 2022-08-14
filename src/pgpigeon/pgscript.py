import os
from .common import PgCommon
from .constants import BASE_PIGEON_FOLDER, PG_SCRIPT_FOLDER


class PgScript:
    def __init__(self):
        self.pg_common = PgCommon()

    def create_scripts(self):
        try:
            pigeon_file_path = self.pg_common.find_config_path()
            print(f":: Pigeon file path = {pigeon_file_path}")
            _database =  self.pg_common.load_configs(pigeon_file_path)
            for _schema in _database["schemas"]:
                for _table in _schema["tables"]:
                    for _trigger in _table["triggers"]:
                        trigger_func_body = self.pg_common.generate_trigger_func_body(
                            _trigger)
                        trigger_body = self.pg_common.generate_trigger_body(
                            _table, _trigger)
                        self.__create_scripts_file(
                            _trigger["trigger_func"], trigger_func_body)
                        self.__create_scripts_file(
                            _trigger["name"], trigger_body)
        except Exception as e:
            print(f":: Error : {e}")

    def __create_scripts_file(self, script_file_name, pg_script):
        cwd = os.getcwd()
        pigeon_scripts_dir = os.path.join(
            cwd, BASE_PIGEON_FOLDER, PG_SCRIPT_FOLDER)
        if not os.path.exists(pigeon_scripts_dir):
            os.mkdir(pigeon_scripts_dir)

        pigeon_json_file = os.path.join(
            cwd, BASE_PIGEON_FOLDER, PG_SCRIPT_FOLDER, f"{script_file_name}.sql")
        with open(pigeon_json_file, 'w') as f:
            f.write(pg_script)
        print(
            f":: Pigeon db script file '{script_file_name}' has been created successfully at location {pigeon_scripts_dir}")
