
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
                                "name": "default_trigger",
                                "trigger_func": "default_trigger_func",
                                "channel_name": "default_channel",
                                "json_build_object_str": "json_build_object('item_no', NEW.item_no,'item_desc', NEW.item_description)",
                                "type": "ROW",
                                "trigger_on": "INSERT",
                                "on_condition": "AFTER",
                                "folder": "",
                                "file": ""
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

def callback_func(channel,payload):
    print(type(payload))
    print(f"Channel : {channel}")
    print(f"Payload : {payload}")

def run():
    pg_nest=PgNest()
    _database={}
    _database["dbname"]="postgres"
    _database["host"]="localhost"
    _database["port"]="5432"
    _database["user"]="postgres"
    _database["password"]="postgres"
    pg_nest.start(_database,"default_channel",callback_func)

if __name__ == "__main__":
    run()
'''

BASE_PIGEON_FOLDER='pigeon'
PG_SCRIPT_FOLDER='scripts'

PIGEON_JSON_FILE='pigeon.json'
PG_PIGEON_SAMPLE_CODE_FILE='pigeon.py'