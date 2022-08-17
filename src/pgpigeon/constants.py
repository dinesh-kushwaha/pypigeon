PIGEON_JSON = ''' 
{
    "dbname": "postgres",
    "host": "localhost",
    "port": "5432",
    "user": "postgres",
    "password": "postgres",
    "schemas": [
        {
            "name": "public",
            "tables": [
                {
                    "name": "items",
                    "triggers": [
                        {
                            "name": "pg_pigeon_default_after_insert_update_delete_trigger",
                            "trigger_func": "pg_pigeon_default_after_insert_update_delete_trigger_func",
                            "channel_name": "pg_pigeon_default_channel",
                            "return_columns": "['item_no', 'item_description']",
                            "type": "ROW",
                            "trigger_on": "INSERT OR UPDATE OR DELETE",
                            "trigger_on_statement": "INSERT OR UPDATE OR DELETE",
                            "on_condition": "AFTER",
                            "is_active": "True"
                        },
                        {
                            "name": "pg_pigeon_default_before_insert_update_delete_trigger",
                            "trigger_func": "pg_pigeon_default_before_insert_update_delete_trigger_func",
                            "channel_name": "pg_pigeon_default_channel_before",
                            "return_columns": "['item_no', 'item_description']",
                            "type": "ROW",
                            "trigger_on": "INSERT OR UPDATE OR DELETE",
                            "trigger_on_statement": "INSERT OR UPDATE OR DELETE",
                            "on_condition": "BEFORE",
                            "is_active": "False"
                        },
                        {
                            "name": "pg_pigeon_default_after_insert_update_trigger",
                            "trigger_func": "pg_pigeon_default_after_insert_update_trigger_func",
                            "channel_name": "pg_pigeon_default_channel",
                            "return_columns": "['item_no', 'item_description']",
                            "type": "ROW",
                            "trigger_on": "INSERT OR UPDATE OR DELETE",
                            "trigger_on_statement": "INSERT OR UPDATE OR DELETE",
                            "on_condition": "AFTER",
                            "is_active": "False"
                        },
                        {
                            "name": "pg_pigeon_default_after_insert_trigger",
                            "trigger_func": "pg_pigeon_default_after_insert_trigger_func",
                            "channel_name": "pg_pigeon_default_channel",
                            "return_columns": "['item_no', 'item_description']",
                            "type": "ROW",
                            "trigger_on": "INSERT",
                            "trigger_on_statement": "INSERT",
                            "on_condition": "AFTER",
                            "is_active": "False"
                        },
                        {
                            "name": "pg_pigeon_default_after_update_trigger",
                            "trigger_func": "pg_pigeon_default_after_update_trigger_func",
                            "channel_name": "pg_pigeon_default_channel",
                            "return_columns": "['item_no', 'item_description']",
                            "type": "ROW",
                            "trigger_on": "UPDATE",
                            "trigger_on_statement": "UPDATE OF item_description",
                            "on_condition": "AFTER",
                            "is_active": "False"
                        },
                        {
                            "name": "pg_pigeon_default_after_delete_trigger",
                            "trigger_func": "pg_pigeon_default_after_delete_trigger_func",
                            "channel_name": "pg_pigeon_default_channel",
                            "return_columns": "['item_no', 'item_description']",
                            "type": "ROW",
                            "trigger_on": "DELETE",
                            "trigger_on_statement": "DELETE",
                            "on_condition": "AFTER",
                            "is_active": "False"
                        },
                        {
                            "name": "pg_pigeon_default_before_insert_trigger",
                            "trigger_func": "pg_pigeon_default_before_insert_trigger_func",
                            "channel_name": "pg_pigeon_default_channel",
                            "return_columns": "['item_no', 'item_description']",
                            "type": "ROW",
                            "trigger_on": "INSERT",
                            "trigger_on_statement": "INSERT",
                            "on_condition": "BEFORE",
                            "is_active": "False"
                        },
                        {
                            "name": "pg_pigeon_default_before_update_trigger",
                            "trigger_func": "pg_pigeon_default_before_update_trigger_func",
                            "channel_name": "pg_pigeon_default_channel",
                            "return_columns": "['item_no', 'item_description']",
                            "type": "ROW",
                            "trigger_on": "UPDATE",
                            "trigger_on_statement": "UPDATE OF item_no , item_description",
                            "on_condition": "BEFORE",
                            "is_active": "False"
                        },
                        {
                            "name": "pg_pigeon_default_instead_of_insert_trigger",
                            "trigger_func": "pg_pigeon_default_instead_of_insert_trigger_func",
                            "channel_name": "pg_pigeon_default_channel",
                            "return_columns": "['item_no', 'item_description']",
                            "type": "ROW",
                            "trigger_on": "INSERT",
                            "trigger_on_statement": "INSERT",
                            "on_condition": "INSTEAD OF",
                            "is_active": "False"
                        },
                        {
                            "name": "pg_pigeon_default_instead_of_update_trigger",
                            "trigger_func": "pg_pigeon_default_instead_of_update_trigger_func",
                            "channel_name": "pg_pigeon_default_channel",
                            "return_columns": "['item_no', 'item_description']",
                            "type": "ROW",
                            "trigger_on": "UPDATE",
                            "trigger_on_statement": "UPDATE OF item_no , item_description",
                            "on_condition": "INSTEAD OF",
                            "is_active": "False"
                        }
                    ]
                }
            ]
        }
    ]
}
'''

PG_PIGEON_SAMPLE_LISTENER_CODE = '''
from pgpigeon.pgnest import PgNest
from pgpigeon.context_models import PigeonChannelContext,PigeonContext, PgExecutionStrategy

class PGPigeonClient:
    def callback_func(self, channel, payload):
        print(f"Channel : {channel}")
        print(f"Payload : {payload}")

    def get_pg_db_dict(self):
        pg_db_dict = {}
        pg_db_dict["dbname"] = "postgres"
        pg_db_dict["host"] = "localhost"
        pg_db_dict["port"] = "5432"
        pg_db_dict["user"] = "postgres"
        pg_db_dict["password"] = "postgres"
        return pg_db_dict

    def start_keep_eye_on_channels_and_notify(self):
        pg_contexts = []

        pg_context = PigeonContext("pg_pigeon_default_process")
        pg_context.execution_strategy = PgExecutionStrategy.IN_SEPARATE_PROCESS
        pg_context.is_main_on_hold = False

        pg_channel = PigeonChannelContext("pg_pigeon_default_channel")
        pg_channel.callbacks.append(self.callback_func)

        pg_context.channels.append(pg_channel)
        pg_contexts.append(pg_context)

        pg_nest = PgNest()
        pg_db_dict = self.get_pg_db_dict()
        pg_nest.start_keep_eye_on_channels_and_notify(
            pg_db_dict, pg_contexts)


if __name__ == "__main__":
    client = PGPigeonClient()
    client.start_keep_eye_on_channels_and_notify()
'''

BASE_PIGEON_FOLDER = 'pigeon'
PG_SCRIPT_FOLDER = 'scripts'

PIGEON_JSON_FILE = 'pigeon.json'
PG_PIGEON_SAMPLE_CODE_FILE = 'pigeon.py'

PG_PIGEON_GIT_IGNORE_FILE = '.gitignore'
PG_PIGEON_GIT_IGNORE = '''
# Ignoring the database related sensitive information to be pushed to repository.
# You can alter this setting.

pigeon.json 

'''
