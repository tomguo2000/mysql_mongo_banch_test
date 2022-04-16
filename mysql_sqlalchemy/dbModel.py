import time
from .db import db
from uuid import UUID, uuid4

class dbModel(db.Model):
    __tablename__ = "banchtest_sqlalchemy"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    message_id = db.Column(db.String(32), index=True)
    parameters = db.Column(db.String(1000))
    create_time = db.Column(db.String(1000))

    def __init__(self):
        # required fields
        self.message_id = uuid4().hex
        self.parameters = uuid4().hex
        self.create_time = str(time.time())

    def json(self):
        return {
            "id": self.id,
            "message_id": self.message_id,
            "parameters": self.parameters,
            "create_time": self.create_time,
        }

    def save_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
            resp = 'sqlalchemy add one success At' + str(id(db)) + '    ' + str(id(db.session))
        except:
            resp = 'sqlalchemy add one error At' + str(id(db)) + '    ' + str(id(db.session))
        return resp

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
