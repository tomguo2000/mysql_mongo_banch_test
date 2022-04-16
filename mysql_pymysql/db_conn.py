
import pymysql

db_conn_pymysql = pymysql.connect(
    host='127.0.0.1',
    port=33006,
    user='message_center',
    passwd='a9U911VU2Ggz',
    db='message_center',
    connect_timeout=30,
    read_timeout=10
)