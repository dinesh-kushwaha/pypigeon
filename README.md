<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">PgPigeon</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> This package will help to capture realtime postgreSQL table notification.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [TODO](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

This package can be used for capture PostgreSQL database table event at real time.

## 🏁 Getting Started <a name = "getting_started"></a>

To Start experimenting this package you need to install it.

Step - 1 
```
pip install pgpigeon
```

Step - 2
Create three files - 
- pigeon.json
- pgpigeon.py
- pgnest.py

Step - 3
Copy paste following contents in  "pigeon.json" file.

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
```


Step - 4
Copy paste following contents in  "pgpigeon.py" file.

```
from pgpigeon.pgpigeon import PgPigeon

pg_pigeon = PgPigeon()
pg_pigeon.init()
```
Above line of code will create required database objects. 

Step - 5 
Copy paste following contents in  "pgnest.py" file.

```
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

pg_nest.listen(_database,"default_channel_1",callback_func)
```
Above line of codes will notification if any change happens in target database table.


### Prerequisites

What things you need to install the software and how to install them.

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running.

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo.

## 🔧 Running the tests <a name = "tests"></a>

Explain how to run the automated tests for this system.

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## 🎈 Usage <a name="usage"></a>

Add notes about how to use the system.

## 🚀 Deployment <a name = "deployment"></a>

Add additional notes about how to deploy this on a live system.

## ⛏️ Built Using <a name = "built_using"></a>

- [MongoDB](https://www.mongodb.com/) - Database
- [Express](https://expressjs.com/) - Server Framework
- [VueJs](https://vuejs.org/) - Web Framework
- [NodeJs](https://nodejs.org/en/) - Server Environment

## ✍️ Authors <a name = "authors"></a>

- [@dinesh-pypi](https://pypi.org/user/dinesh-pypi/) - Idea & Initial work

See also the list of [contributors](https://github.com/dinesh-kushwaha) who participated in this project.

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Hat tip to anyone whose code was used
- Inspiration
- References
