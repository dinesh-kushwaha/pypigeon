import json
import os

from .constants import BASE_PIGEON_FOLDER, PG_SCRIPT_FOLDER, PIGEON_JSON_FILE


class PgCommon:
    
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
        trigger_on = _trigger["trigger_on"]
        channel_name = _trigger["channel_name"]
        json_build_object_str = _trigger["json_build_object_str"]
        sql = f'''
        CREATE OR REPLACE FUNCTION {trigger_func_name}()
                RETURNS trigger
                LANGUAGE 'plpgsql'
            as $$
            declare
            begin
                if (tg_op = '{trigger_on}') then
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
        trigger_on = _trigger["trigger_on"]
        on_condition = _trigger["on_condition"]
        sql = f'''
        CREATE OR REPLACE TRIGGER {trigger_name}
            {on_condition} {trigger_on}
            ON {table_name}
            FOR EACH {trigger_type}
            EXECUTE PROCEDURE {trigger_func_name}();
        '''
        return sql