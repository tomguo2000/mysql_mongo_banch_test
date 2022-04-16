from flask import Flask, request
import logging
from logging.handlers import SMTPHandler
import json
import pymysql
from mysql_sqlalchemy.dbModel import dbModel
from mongo_pymongo.mongo_add_one import add_one_mongo
from mysql_pymysql.POOL_2 import SingletonDBPool
from uuid import uuid4
import time

pymysql.install_as_MySQLdb()


logger = logging.getLogger()
logger.setLevel(logging.INFO)
LOG_FILENAME = 'webhook.log'

fh = logging.handlers.TimedRotatingFileHandler(
    LOG_FILENAME, when="midnight", interval=1, backupCount=90, encoding="utf-8", delay=False)
ch = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(process)d-%(threadName)s - '
                              '%(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://message_center:a9U911VU2Ggz@127.0.0.1:33006/message_center"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.url_map.strict_slashes = False


from mysql_sqlalchemy.db import db
db.init_app(app)


@app.route('/mysql',  methods=['GET'])
def mysql_get():
    logger.info(f"MESSAGE: mysql_get: {request.url}")

    return {'code': 200}


@app.route('/mysql/sqlalchemy', methods=['GET'])
def sqlalchemy_add_one():

    one = dbModel()
    result = one.save_to_db()
    logger.info(result)
    return {
        'code': 200,
        'message': 'add one to sqlalchemy mysql',
        'businessObj': result
    }


@app.route('/mysql/pymysql', methods=['GET'])
def pymysql_add_one():
    pool = SingletonDBPool()
    conn = pool.connect()
    cursor = conn.cursor()
    inser_sql = 'insert into banchtest_pymysql (message_id, parameters, create_time) values (%s, %s, %s)'
    values = (uuid4().hex, uuid4().hex, str(time.time()))
    cursor.execute(inser_sql, values)
    conn.commit()

    return {
        'code': 200,
        'message': 'add one to sqlalchemy mysql',
        'businessObj': None
    }

@app.route('/mysql/pymysql/count', methods=['GET'])
def pymysql_count():
    pool = SingletonDBPool()
    conn = pool.connect()
    cursor = conn.cursor()

    sql='select count(*) from banchtest_pymysql'
    cursor.execute(sql)
    resp = cursor.fetchall()
    print(resp)
    print(type(resp))

    return {
        'code': 200,
        'message': 'count all records',
        'businessObj': resp
    }


@app.route('/mongo', methods=['GET'])
def mongo_add_one():

    result = add_one_mongo()
    logger.info("pymysql add one")

    return {
        'code': 200,
        'message': 'add one to mongo',
        'businessObj': result
    }


@app.route('/webhook',  methods=['POST'])
def webhook():
    logger.info(f"MESSAGE: {request.data.decode()}")
    return {'code': 200}


@app.route('/webhook/get', methods=['GET'])
def webhook_get():
    logger.info(f"MESSAGE: {request.url}")
    return {'code': 200}


@app.route('/response_put', methods=['PUT'])
def response_put():
    logger.info(f"MESSAGE_URL: {request.url}. MESSAGE_FORM_DATA: {request.form}. MESSAGE_BODY: {request.data}")
    return {'code': 200}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5678, use_reloader=False)

