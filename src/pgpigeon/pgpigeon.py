from time import sleep
import psycopg2
from .common import PgCommon


class PgPigeon:
    def __init__(self):
        self.channels = []
        self.pg_common = PgCommon()

    def execute_pgsql_query(self, _database, pgsql_query):
        try:
            self.connection = psycopg2.connect(
                dbname=_database["dbname"], user=_database["user"], host=_database["host"], port=_database["port"], password=_database["password"])
            self.connection.set_isolation_level(
                psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
            cur = self.connection.cursor()
            cur.execute(pgsql_query)
            print(
                f":: Pg database object created successfully : {pgsql_query}")
        except Exception as e:
            print(f":: Error : {e}")

    def create_triggers(self):
        try:
            pigeon_file_path = self.pg_common.find_config_path()
            print(f":: Pigeon file path = {pigeon_file_path}")
            _database = self.pg_common.load_configs(pigeon_file_path)
            for _schema in _database["schemas"]:
                for _table in _schema["tables"]:
                    for _trigger in _table["triggers"]:
                        trigger_func_body = self.pg_common.generate_trigger_func_body(
                            _trigger)
                        trigger_body = self.pg_common.generate_trigger_body(
                            _table, _trigger)
                        self.__execute_triggers(
                            _database, trigger_func_body, trigger_body)
        except Exception as e:
            print(f":: Error : {e}")

    def __execute_triggers(self, _database, trigger_func_body, trigger_body):
        try:
            self.execute_pgsql_query(_database, trigger_func_body)
            self.execute_pgsql_query(_database, trigger_body)
        except Exception as e:
            print(f":: Error : {e}")
