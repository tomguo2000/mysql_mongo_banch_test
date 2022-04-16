from .db_conn import db_conn_pymysql
from uuid import uuid4
import datetime

def add_one(db_cur):
    try:
        inser_sql = 'insert into banchtest_pymysql (message_id, parameters, create_time) values (%s, %s, %s)'
        values = (uuid4().hex, uuid4().hex, datetime.datetime.now())
        db_cur.execute(inser_sql, values)
        db_conn_pymysql.commit()
        return True
    except:
        return False
