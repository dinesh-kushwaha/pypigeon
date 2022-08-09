import psycopg2
import select
from pg.models.db_channel_config import DbChannelConfig
from pg.models.db_config import DbConfig


class PgListener:
    def __init__(self, db_config:DbConfig,db_channel_config:DbChannelConfig,call_back):
        self.db_config = db_config
        self.db_channel_config=db_channel_config
        self.call_back=call_back
        self.connection= psycopg2.connect(dbname=db_config.dbname, user=db_config.user, host=db_config.host, port=db_config.port, password=db_config.password)

    
    #listen to channel 
    def listen(self):
        #set to autocommit
        self.connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        cur = self.connection.cursor()
        cur.execute(f"LISTEN {self.db_channel_config.channel_name};")
        print(f":: Listning .....")
        while True:
            print(f":: Running .....")
            print(f":: Sleep until there is some data ....")
            select.select([self.connection],[],[])   #sleep until there is some data
            print(f":: Get the message....")
            self.connection.poll()                   #get the message
            while self.connection.notifies:
                print('got the message....')
                notification =  self.connection.notifies.pop()  #pop notification from list
                #now do anything needed! 
                print(f"channel: {notification.channel }")
                print(f"message: {notification.payload}")
                self.call_back()
            

