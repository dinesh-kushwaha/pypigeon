from time import sleep
import psycopg2
from .common import PgCommon


class PgPigeon:
    def __init__(self):
        self.channels = []
        self.pg_common = PgCommon()

    def execute_pgsql_query(self, _database, schema, pgsql_query):
        try:
            self.connection = psycopg2.connect(
                dbname=_database["dbname"], user=_database["user"], host=_database["host"], port=_database["port"], password=_database["password"])
            self.connection.set_isolation_level(
                psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
            cur = self.connection.cursor()
            search_path_sql = f"SET search_path TO {schema};"
            print(f":: {search_path_sql}")
            cur.execute(search_path_sql)
            print(f":: Script body : {pgsql_query}")
            cur.execute(pgsql_query)
            print(
                f":: PostgreSQL query executed successfully.")
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
                        if not eval(_trigger["is_active"]):
                            continue
                        trigger_func_clean_up_sql, trigger_func_body_sql = self.pg_common.generate_trigger_func_body(
                            _trigger)
                        _schema_name = _schema["name"]
                        self.__execute_triggers(
                            _database, _schema_name, trigger_func_clean_up_sql, trigger_func_body_sql)
                        trigger_clean_up_sql, trigger_body_sql = self.pg_common.generate_trigger_body(
                            _table, _trigger)
                        self.__execute_triggers(
                            _database, _schema_name, trigger_clean_up_sql, trigger_body_sql)

        except Exception as e:
            print(f":: Error : {e}")

    def __execute_triggers(self, _database, schema, clean_up_sql, sql):
        try:
            self.execute_pgsql_query(_database, schema, clean_up_sql)
            self.execute_pgsql_query(_database, schema, sql)
        except Exception as e:
            print(f":: Error : {e}")
