<h3 align="center">PgPigeon</h3>

<p align="center"> This package will help to capture realtime postgreSQL table notification in python scripts.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>

This package can be used for capture PostgreSQL database table event at real time in python scripts.

## 🏁 Getting Started <a name = "getting_started"></a>

To Start experimenting this package you need to install it.

Step - 1 
```
pip install pgpigeon
```

Step - 2
    To configure pigeon 
    ```
    pigeon configure
    ```
    This will create the configuration file "pigeon.json" in "pigeon" folder.
    In this file you can see database related settings i.e. database , schema , tables and triggers.

Step - 3
    To generate the db scripts i.e. triggers run following command 
    ```
    pigeon create-scripts
    ```
    This will create all the required scripts in "pigeon/scripts" folder. 
    Two scripts files will be created on for trigger function and second trigger.

Step - 4
    To create the triggers in database i.e. run following command 
    ```
    pigeon create-triggers
    ```
    This will create required triggers in database. 
Step - 5
    To create sample code run following command 
    ```
    pigeon sample-code
    ```
    This will create sample code in "pigeon.py". 

Now you an hook "pigeon.py" sample code anywhere in your code logic.
It will start notifying if any change happen in the target db tables.


Let's review "pigeon.json" configuration file. 

```
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
```

Now you can see above json config file having all the details in order to create trigger for notification.
i.e. database connection details for connectivity , schema , table and trigger info to create triggers.

Note - 
```
"channel_name": "default_channel"
```
"channel_name" is the property responsible to communicate with python script.

"json_build_object_str" is the json property responsible to send notification payload to python script.
This property value should be look like below one.

```
"json_build_object_str": "json_build_object('item_no', NEW.item_no,'item_desc', NEW.item_description)"
```

For example - as mentioned in json config file.
if we have a table "items" structure like 

```
CREATE TABLE public.items (
    item_id serial PRIMARY KEY,
	item_no int4 NULL,
	item_description varchar NULL,
    created_on TIMESTAMP NOT NULL,
    last_login TIMESTAMP 
);
```
then this property should be look like 
```
"json_build_object_str": "json_build_object('item_no', NEW.item_no,'item_desc', NEW.item_description)"
```
all the keys are table column names.

Let's review the sample code .

```
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
```

From above sample code you can see the python script is listening the channel for notification.
Once your script is successfully running you will see the logs.
```
    :: Listening channel : default_channel
    :: Running .....
    :: Sleep until there is some data ....
```

if you insert any record in target db table you will see this logs.
```
    :: Listening channel : default_channel
    :: Running .....
    :: Sleep until there is some data ....
    :: Get the message....
    got the message....
    Channel : default_channel
    Payload : {"item_no" : 232342, "item_desc" : "Testing..."}
    :: Running .....
    :: Sleep until there is some data ....
```

Now you can dieselize the payload and you can do anything with it.

## ✍️ Authors <a name = "authors"></a>

- [Dinesh Kushwaha](https://pypi.org/user/dinesh-pypi/) - Idea & Initial work

See also the list of [contributors](https://github.com/dinesh-kushwaha) who participated in this project.