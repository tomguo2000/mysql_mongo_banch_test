from flask import Flask, request
import logging
from logging.handlers import SMTPHandler
import pymysql
from mysql_sqlalchemy.dbModel import dbModel
from mongo_pymongo.mongo_add_one import add_one_mongo
from mysql_pymysql.pymysql_pool_class_opt import add_one_mysql_pool_class
from mysql_pymysql.pymysql_pool_file_opt import add_one_mysql_pool_file, count_all
from mongo_mongoengine.mongo_with_mongoengine import add_movie


from config import MYSQL_URI

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


app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://message_center:a9U911VU2Ggz@{MYSQL_URI}:33006/message_center"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.url_map.strict_slashes = False

app.config['MONGODB_SETTINGS'] = {
    'db': 'mongo_banchmark',
    'host': MYSQL_URI,
    'port': 27017,
    # 'username': 'admin',
    # 'password': '123456',
    # 'authentication_source': 'admin'
}


from mysql_sqlalchemy.db import db
db.init_app(app)

from mongo_mongoengine.mongo_me import db_me
db_me.init_app(app)


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


@app.route('/mysql/pymysql/file', methods=['GET'])
def pymysql_file_add_one():
    add_one_mysql_pool_file()

    return {
        'code': 200,
        'message': 'add one to sqlalchemy mysql',
        'businessObj': None
    }



@app.route('/mysql/pymysql/class', methods=['GET'])
def pymysql_class_add_one():
    add_one_mysql_pool_class()

    return {
        'code': 200,
        'message': 'add one to sqlalchemy mysql',
        'businessObj': None
    }



@app.route('/mysql/pymysql/count', methods=['GET'])
def pymysql_count():

    return {
        'code': 200,
        'message': 'count all records',
        'businessObj': count_all()
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


@app.route('/mongo/me', methods=['GET'])
def mongo_add_one_me():

    result = add_movie()
    logger.info("mongo_engine add one")

    return {
        'code': 200,
        'message': 'add one to mongo by using mongo_engine',
        'businessObj': result
    }

#
# @app.route('/mongo/total', methods=['GET'])
# def mongo_total():
#
#     result = add_one_mongo()
#     logger.info("pymysql add one")
#
#     return {
#         'code': 200,
#         'message': 'add one to mongo',
#         'businessObj': result
#     }


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

