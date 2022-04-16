from .POOL_class import SingletonDBPool
from uuid import uuid4
import time
pool = SingletonDBPool()

def add_one_mysql_pool_class():

    conn = pool.connect()
    cursor = conn.cursor()
    inser_sql = 'insert into banchtest_pymysql (message_id, parameters, create_time) values (%s, %s, %s)'
    values = (uuid4().hex, uuid4().hex, str(time.time()))
    cursor.execute(inser_sql, values)
    conn.commit()