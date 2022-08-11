import psycopg2
import select


class PgNest:
    
    def listen(self, _database, channel_name, callback_func):
        self.connection = psycopg2.connect(
            dbname=_database["dbname"], user=_database["user"], host=_database["host"], port=_database["port"], password=_database["password"])
        self.connection.set_isolation_level(
            psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        cur = self.connection.cursor()
        print()
        pg_sql=f"LISTEN {channel_name};"
        cur.execute(pg_sql)
        print(f":: Listning channel : {channel_name}")
        while True:
            print(f":: Running .....")
            print(f":: Sleep until there is some data ....")
            # sleep until there is some data
            select.select([self.connection], [], [])
            print(f":: Get the message....")
            self.connection.poll()  # get the message
            while self.connection.notifies:
                print('got the message....')
                notification = self.connection.notifies.pop()  # pop notification from list
                # now do anything needed!
                # print(f"channel: {notification.channel }")
                # print(f"message: {notification.payload}")
                callback_func(notification.channel, notification.payload)
