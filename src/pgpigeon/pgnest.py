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
            print(
                f"Main or parent , process or thread with PID {os.getppid()} is blocked.")
            for listener in listeners:
                listener.join()
        else:
            print(f"Pg execution strategy is IN_SEPARATE_THREAD")
            print(
                f"Main or parent , process or thread with PID {os.getppid()} is running.")

    def listeners(self, db_conn_dict, channels):
        for channel in channels:
            self.listen(db_conn_dict, channel.name, channel.callbacks)

    def get_callback_by_channel(self, current_channel, channels):
        callbacks = None
        for channel in channels:
            if channel.name == current_channel:
                callbacks = channel.callbacks
                break
        return callbacks

    def listeners(self, db_conn_dict, channels):
        try:
            self.connection = psycopg2.connect(
                dbname=db_conn_dict["dbname"], user=db_conn_dict["user"], host=db_conn_dict["host"], port=db_conn_dict["port"], password=db_conn_dict["password"])
            self.connection.set_isolation_level(
                psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
            cur = self.connection.cursor()
            for channel in channels:
                pg_sql = f"LISTEN {channel.name};"
                cur.execute(pg_sql)
                print(f":: Listening channel : {channel.name}")
            while True:
                print(
                    f":: Parent process id , name  : {os.getppid()} ")
                print(
                    f":: Current process id , name  : {os.getpid()} ")
                print(f":: Waiting for new messages payload ....")
                select.select([self.connection], [], [])
                self.connection.poll()
                while self.connection.notifies:
                    notification = self.connection.notifies.pop()
                    print(
                        f":: Message payload received from channel {notification.channel} : {notification.payload} ")
                    _callbacks = self.get_callback_by_channel(
                        notification.channel, channels)
                    if not _callbacks:
                        return
                    for callback in _callbacks:
                        callback(notification.channel, notification.payload)
        except Exception as e:
            print(f":: Exception - {e}")
