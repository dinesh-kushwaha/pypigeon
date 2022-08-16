import psycopg2
import select
import multiprocessing
import threading
import os
from .context_models import PgExecutionStrategy


class PgNest:

    def start_keep_eye_on_channels_and_notify(self, db_conn_dict, pigeon_context):
        listeners = []
        for config in pigeon_context:
            listener = None
            if config.execution_strategy == PgExecutionStrategy.IN_SEPARATE_PROCESS:
                listener = multiprocessing.Process(
                    target=self.listeners,
                    name=config.name,
                    args=(db_conn_dict, config.channels, ))
            elif config.execution_strategy == PgExecutionStrategy.IN_SEPARATE_THREAD:
                listener = threading.Thread(target=self.listeners,
                                            name=config.name,
                                            args=(db_conn_dict, config.channels, ))
            if not listener:
                continue
            listeners.append(listener)

        for listener in listeners:
            listener.start()

        if config.is_main_on_hold:
            print(f"Pg execution strategy is IN_SEPARATE_PROCESS")
            for listener in listeners:
                listener.join()
        else:
            print(f"Pg execution strategy is IN_SEPARATE_THREAD")

    def listeners(self, db_conn_dict, channels):
        for channel in channels:
            self.listener(db_conn_dict, channel.name, channel.callbacks)

    def listener(self, db_conn_dict, channel_name, callbacks):
        listener_trd = threading.Thread(target=self.listen,
                                        args=(db_conn_dict, channel_name, callbacks, ))
        listener_trd.start()
        listener_trd.join()

    def listen(self, db_conn_dict, channel_name, callbacks):
        self.connection = psycopg2.connect(
            dbname=db_conn_dict["dbname"], user=db_conn_dict["user"], host=db_conn_dict["host"], port=db_conn_dict["port"], password=db_conn_dict["password"])
        self.connection.set_isolation_level(
            psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        cur = self.connection.cursor()
        pg_sql = f"LISTEN {channel_name};"
        cur.execute(pg_sql)
        print(f":: Listening channel : {channel_name}")
        while True:
            print(
                f":: Parent process id , name  : {os.getppid()} ")
            print(
                f":: Current process id , name  : {os.getpid()} ")
            print(f":: Waiting for new messages payload ....")
            # sleep until there is some data
            select.select([self.connection], [], [])
            self.connection.poll()  # get the message
            while self.connection.notifies:
                notification = self.connection.notifies.pop()  # pop notification from list
                print(
                    f":: Message payload received from channel {notification.channel}): {notification.payload} ")
                for callback in callbacks:
                    callback(notification.channel, notification.payload)
