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

- To Start experimenting this package you need to install it.

- [Step - 1]
```

    pip install pgpigeon

```

- [Step - 2]
    - To configure pigeon 
    ```

    pigeon configure

    ```
    This will create the configuration file "pigeon.json" in "pigeon" folder.
    In this file you can see database related settings i.e. database , schema , tables and triggers.

- [Step - 3] 
    - [To generate the db scripts i.e. triggers run following command ]
    ``` 

    pigeon create-scripts

    ```
    This will create all the required scripts in "pigeon/scripts" folder. 
    Two scripts files will be created on for trigger function and second trigger.

- [Step - 4]
    - To create the triggers in database i.e. run following command 
    ```


    pigeon create-triggers

    ```
    This will create required triggers in database. 
- [Step - 5]
    - To create sample code run following command 
    ```

    pigeon sample-code

    ```
    This will create sample code in "pigeon.py". 

Now you an hook "pigeon.py" sample code anywhere in your code logic.
It will start notifying if any change happen in the target db tables.


- Let's review "pigeon.json" configuration file. 

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
```

Now you can see above json config file having all the details in order to create trigger for notification.
i.e. database connection details for connectivity , schema , table and trigger info to create triggers.

Note - 
```

"channel_name": "pg_pigeon_default_channel"

```
"channel_name" is the property responsible to communicate with python script.

"return_columns" is the json property responsible to send notification payload to python script.
This property value should be look like below one.

```

"return_columns": "['item_no', 'item_description']"

```

For example - as mentioned in json config file.
if we have a table "items" structure like 

```
CREATE TABLE public.items (
	item_no int4 NULL,
	item_description varchar NULL
);

```
then this property should be look like 
```
"return_columns": "['item_no', 'item_description']"
```
all the keys are table column names.

Let's review the sample code .

```
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
        # If you set is_main_on_hold=True , main thread or process will be blocked.
        # If you set is_main_on_hold=False , main thread or process will keep running.
        pg_context.is_main_on_hold = True

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
```

From above sample code you can see the python script is listening the channel for notification.
Once your script is successfully running you will see the logs.
```
:: Parent process id , name  : 23512:: Current process id , name  : 19768
:: Waiting for new messages payload ....
```

if you insert or update or delete any record in target db table you will see this logs.
```
:: Current process id , name  : 19768
:: Waiting for new messages payload ....
:: Message payload received from channel pg_pigeon_default_channel): {"item_no" : 1, "item_description" : "23523523", "action" : "INSERT"}
Channel : pg_pigeon_default_channel
Payload : {"item_no" : 1, "item_description" : "23523523", "action" : "INSERT"}
:: Parent process id , name  : 23512:: Current process id , name  : 19768
:: Waiting for new messages payload ....
:: Message payload received from channel pg_pigeon_default_channel): {"item_no" : 1, "item_description" : "dinesh kushwaha", "action" : "UPDATE"}
Channel : pg_pigeon_default_channel
Payload : {"item_no" : 1, "item_description" : "dinesh kushwaha", "action" : "UPDATE"}
:: Parent process id , name  : 23512:: Current process id , name  : 19768
:: Waiting for new messages payload ....
:: Message payload received from channel pg_pigeon_default_channel): {"item_no" : 1, "item_description" : "dinesh kushwaha", "action" : "DELETE"}
Channel : pg_pigeon_default_channel
Payload : {"item_no" : 1, "item_description" : "dinesh kushwaha", "action" : "DELETE"}
:: Parent process id , name  : 23512:: Current process id , name  : 19768
:: Waiting for new messages payload ....
```

Now you can dieselize the payload and you can do anything with it.

## ✍️ Authors <a name = "authors"></a>

- [Dinesh Kushwaha](https://pypi.org/user/dinesh-pypi/) - Idea & Initial work

See also the list of [contributors](https://github.com/dinesh-kushwaha) who participated in this project.