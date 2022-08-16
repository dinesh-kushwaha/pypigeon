from pgpigeon.pgnest import PgNest
from pgpigeon.process_config import PigeonChannel, PigeonContext, PgExecutionStrategy


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

    # This method will listen multiple channels at a time
    # in a septate python process each channels

    def start_keep_eye_on_channels_and_notify(self):
        process_configs = []
        process_config = PigeonContext("pg_pigeon_default_process")
        process_config.execution_strategy = PgExecutionStrategy.IN_SEPARATE_PROCESS
        process_config.is_main_on_hold = False
        pg_channel = PigeonChannel("pg_pigeon_default_channel")
        pg_channel.callbacks.append(self.callback_func)
        process_config.channels.append(pg_channel)
        process_configs.append(process_config)
        pg_nest = PgNest()
        pg_db_dict = self.get_pg_db_dict()
        pg_nest.start_keep_eye_on_channels_and_notify(
            pg_db_dict, process_configs)


if __name__ == "__main__":
    client = PGPigeonClient()
    client.start_keep_eye_on_channels_and_notify()
