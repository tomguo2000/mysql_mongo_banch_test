from .POOL_file import POOL
from uuid import uuid4
import time

def add_one_mysql_pool_file():
    conn = POOL.connection()
    cursor = conn.cursor()
    inser_sql = 'insert into banchtest_pymysql (message_id, parameters, create_time) values (%s, %s, %s)'
    values = (uuid4().hex, uuid4().hex, str(time.time()))
    cursor.execute(inser_sql, values)
    conn.commit()


def count_all():
    conn = POOL.connection()
    cursor = conn.cursor()

    sql='select count(*) from banchtest_pymysql'
    cursor.execute(sql)
    return cursor.fetchall()
