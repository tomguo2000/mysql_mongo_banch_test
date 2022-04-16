import pymysql
from uuid import uuid4
import time

class Con_db(object):
    db = []
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self):
        self.db_host = '47.100.138.122'
        # self.db_host = '127.0.0.1'
        self.db_port = 33006
        self.db_user = 'message_center'
        self.db_password = 'a9U911VU2Ggz'
        self.db_database = 'message_center'
        self.db = pymysql.connect(
            host=self.db_host,
            user=self.db_user,
            port=self.db_port,
            database=self.db_database,
            password=self.db_password
        )

class DBConnection(Con_db):
    def __init__(self):
        super().__init__()

    def get_count(self):
        sql = 'select count(*) from banchtest_pymysql'
        con_cursor = self.db.cursor()
        con_cursor.execute(sql)
        data = con_cursor.fetchall()
        return data

    def insert_one(self):
        inser_sql = 'insert into banchtest_pymysql (message_id, parameters, create_time) values (%s, %s, %s)'
        values = (uuid4().hex, uuid4().hex, str(time.time()))
        con_cursor = self.db.cursor()
        con_cursor.execute(inser_sql, values)
        self.db.commit()


if __name__ == '__main__':
    a1=DBConnection()
    print(a1.get_count())
    for x in range(100):
        a1.insert_one()
    print(a1.get_count())