import pymysql
import threading
from dbutils.pooled_db import PooledDB
from config import MYSQL_URI

class SingletonDBPool(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        self.pool = PooledDB(
            creator=pymysql,
            maxconnections=10,
            mincached=2,
            maxcached=5,
            maxshared=3,
            blocking=True,
            maxusage=None,
            setsession=[],
            ping=0,
            host=MYSQL_URI,
            port=33006,
            user='message_center',
            password='a9U911VU2Ggz',
            database='message_center',
            charset='utf8'
        )

    def __new__(cls, *args, **kwargs):
        if not hasattr(SingletonDBPool, "_instance"):
            with SingletonDBPool._instance_lock:
                if not hasattr(SingletonDBPool, "_instance"):
                    SingletonDBPool._instance = object.__new__(cls, *args, **kwargs)
        return SingletonDBPool._instance

    def connect(self):
        return self.pool.connection()
