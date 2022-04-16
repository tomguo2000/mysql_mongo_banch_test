import pymongo
from pymongo.errors import AutoReconnect


def retry_if_auto_reconnect_error(exception):
    """Return True if we should retry (in this case when it's an AutoReconnect), False otherwise"""
    return isinstance(exception, AutoReconnect)

try:

    mongo = pymongo.MongoClient('127.0.0.1:27017', True)

    db = mongo['mongo_banchmark']

    mongo.server_info()  #trigger exception if cannot connect to db

except:
    print("ERROR - Cannot connect to db")
    pass
