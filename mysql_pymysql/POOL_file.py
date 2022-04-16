import time
import pymysql
import threading
from dbutils.pooled_db import PooledDB, SharedDBConnection
from config import MYSQL_URI
POOL = PooledDB(
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
