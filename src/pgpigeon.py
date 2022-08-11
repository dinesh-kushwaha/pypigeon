import psycopg2
import json
import os
from traceback import print_tb
from pg.models.pigeon_option import PigeonDatabase, PigeonOption

from pg.pgnest import PgListener
# from pg.models.db_channel_config import DbChannelConfig
# from pg.models.db_config import DbConfig


class PgPigeon:
    def __init__(self):
        self.channels = []

    def load_configs(self, pigeon_file_path):
        try:
            f = open(pigeon_file_path)
            data = json.load(f)
            f.close()
            return data
        except Exception as e:
            print(e)

    def find_config_path(self):
        pigeon_file = 'pigeon.json'
        pigeon_file_path = "./pigeon.json"
        for root, dirs, files in os.walk(os.path.abspath(os.curdir)):
            for name in files:
                if name == pigeon_file:
                    pigeon_file_path = os.path.abspath(
                        os.path.join(root, name))
                    break
        return pigeon_file_path

    def genrate_trigger_func_body(self, _trigger):
        trigger_func_name = _trigger["trigger_func"]
        trigger_on = _trigger["triger_on"]
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

    def genrate_trigger_body(self, _table, _trigger,):
        table_name = _table["name"]
        trigger_name = _trigger["name"]
        trigger_type = _trigger["type"]
        trigger_func_name = _trigger["trigger_func"]
        trigger_on = _trigger["triger_on"]
        on_condition = _trigger["on_condition"]
        sql = f'''
        CREATE OR REPLACE TRIGGER {trigger_name}
            {on_condition} {trigger_on}
            ON {table_name}
            FOR EACH {trigger_type}
            EXECUTE PROCEDURE {trigger_func_name}();
        '''
        return sql

    def execute_pgsql_query(self, _database, pgsql_query):
        try:
            self.connection = psycopg2.connect(
                dbname=_database["dbname"], user=_database["user"], host=_database["host"], port=_database["port"], password=_database["password"])
            self.connection.set_isolation_level(
                psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
            cur = self.connection.cursor()
            cur.execute(pgsql_query)
            print(f":: Object created sucessfully : {pgsql_query}")
        except Exception as e:
            print(f":: Error : {e}")

    def init(self):
        try:
            pigeon_file_path = self.find_config_path()
            print(f":: Pigeon file path = {pigeon_file_path}")
            _database = self.load_configs(pigeon_file_path)
            for _schema in _database["schemas"]:
                    #print(f":: Schema = {_schema}")
                    for _table in _schema["tables"]:
                        #print(f":: Table = {_table}")
                        for _trigger in _table["triggers"]:
                            # self.execute_pgsql_query(
                            #     _database, trigger_func_body)
                            self.start(_database, self.genrate_trigger_func_body(
                                _trigger), self.genrate_trigger_body(
                                _table, _trigger))
                            # self.execute_pgsql_query(_database, trigger_body)
        except Exception as e:
            print(f":: Error : {e}")

    def start(self, _database, trigger_func_body, trigger_body):
        try:
            self.execute_pgsql_query(_database, trigger_func_body)
            self.execute_pgsql_query(_database, trigger_body)
        except Exception as e:
            print(f":: Error : {e}")


# pg_pigeon = PgPigeon()
# pg_pigeon.init()
