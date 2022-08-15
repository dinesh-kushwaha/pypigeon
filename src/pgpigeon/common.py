import json
import os
from .constants import BASE_PIGEON_FOLDER, PIGEON_JSON_FILE


class PgCommon:

    def is_pigeon_config_available(self):
        cwd = os.getcwd()
        pigeon_json_file = os.path.join(
            cwd, BASE_PIGEON_FOLDER, PIGEON_JSON_FILE)
        return os.path.exists(pigeon_json_file)

    def load_configs(self, pigeon_file_path):
        try:
            f = open(pigeon_file_path)
            data = json.load(f)
            f.close()
            return data
        except Exception as e:
            print(e)

    def find_config_path(self):
        pigeon_file = PIGEON_JSON_FILE
        pigeon_file_path = "./pigeon.json"
        for root, dirs, files in os.walk(os.path.abspath(os.curdir)):
            for name in files:
                if name == pigeon_file:
                    pigeon_file_path = os.path.abspath(
                        os.path.join(root, name))
                    break
        return pigeon_file_path

    def generate_trigger_func_body(self, _trigger):
        trigger_func_name = _trigger["trigger_func"]
        trigger_on_str = _trigger["trigger_on"]
        triggers_on = trigger_on_str.upper().split("OR")
        _tg_ops = []
        for _tg_op in triggers_on:
            _tg_ops.append(f"tg_op = '{_tg_op.strip()}'")
        final_tg_op = ' OR '.join(_tg_ops)
        channel_name = _trigger["channel_name"]
        return_columns = eval(_trigger["return_columns"])
        json_build_object_array = []
        for column in return_columns:
            json_build_object_array.append(
                f"'{column}', CASE WHEN tg_op = 'DELETE' THEN OLD.{column} ELSE NEW.{column} END ")
        json_build_object_array.append(f"'action',tg_op")
        json_build_object_str = f"json_build_object({','.join(json_build_object_array)})"
        sql = f'''
        CREATE OR REPLACE FUNCTION {trigger_func_name}()
                RETURNS trigger
                LANGUAGE 'plpgsql'
            as $$
            declare
            begin
                if ({final_tg_op}) then
                    perform pg_notify('{channel_name}',
                    {json_build_object_str}::text);
                end if;
                return null;
            end
            $$;
        '''
        return sql

    def generate_trigger_body(self, _table, _trigger,):
        table_name = _table["name"]
        trigger_name = _trigger["name"]
        trigger_type = _trigger["type"]
        trigger_func_name = _trigger["trigger_func"]
        trigger_on_statement = _trigger["trigger_on_statement"]
        on_condition = _trigger["on_condition"]
        sql = f'''
        CREATE OR REPLACE TRIGGER {trigger_name}
            {on_condition} {trigger_on_statement}
            ON {table_name}
            FOR EACH {trigger_type}
            EXECUTE PROCEDURE {trigger_func_name}();
        '''
        return sql
