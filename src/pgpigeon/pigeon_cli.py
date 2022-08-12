import sys

from src.pgpigeon.pgpigeon import PgPigeon

json_data='''
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
                                "triger_on": "INSERT",
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

sample_code='''
from pgpigeon.pgnest import PgNest

def callback_func(channel,payload):
    print(type(payload))
    print(f"Channel : {channel}")
    print(f"Payload : {payload}")


pg_nest=PgNest()
_database={}
_database["dbname"]="postgres"
_database["host"]="localhost"
_database["port"]="5432"
_database["user"]="postgres"
_database["password"]="postgres"

pg_nest.listen(_database,"default_channel",callback_func)
'''

def init():
    if len(sys.argv)<2:
        print(f":: Please specify the command.")

    init_arg=sys.argv[1]
    if init_arg=="init":
        with open('pigeon.json', 'w') as f:
            f.write(json_data)

        with open('pigeon.py', 'w') as f:
            f.write(sample_code)
     

def create_trigger():
    pg_pigeon = PgPigeon()
    pg_pigeon.init()

    
    