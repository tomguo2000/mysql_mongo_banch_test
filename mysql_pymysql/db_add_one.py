from .db_conn import db_conn
from uuid import uuid4
import datetime

def add_one():
    db_cur = db_conn.cursor()

    inser_sql = 'insert into banchtest_pymysql (message_id, parameters, create_time) values (%s, %s, %s)'
    values = (uuid4().hex, uuid4().hex, datetime.datetime.now())

    db_cur.execute(inser_sql, values)

    db_conn.commit()
    db_cur.close()
    return None
