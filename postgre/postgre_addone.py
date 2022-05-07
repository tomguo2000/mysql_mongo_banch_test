import time
import json
from dbconfig import connection, cur
from uuid import uuid4

def add_one_postgre():

    inser_sql = 'insert into banchtest_postgre (message_id, parameters, create_time) values (%s, %s, %s)'
    values = (uuid4().hex, uuid4().hex, str(time.time()))
    cur.execute(inser_sql, values)
    connection.commit()

    return True


def get_total_postgre():
    cur.execute("SELECT count(*) from banchtest_postgre")

    return cur.fetchall()


