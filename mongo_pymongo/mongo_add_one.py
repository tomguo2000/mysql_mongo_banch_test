import datetime
import json
from .dbconfig import db
from uuid import uuid4

def add_one_mongo():
    contents = {
        "message_id": uuid4().hex,
        "parameters": uuid4().hex,
        "create_time": datetime.datetime.now()
    }

    return db.event.insert_one(json.loads(contents))
