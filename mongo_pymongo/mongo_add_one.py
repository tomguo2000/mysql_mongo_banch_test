import time
import json
from .dbconfig import db
from uuid import uuid4

def add_one_mongo():
    contents = {
        "message_id": uuid4().hex,
        "parameters": uuid4().hex,
        "create_time": time.time()
    }

    resp = db.event.insert_one(contents)
    return True
