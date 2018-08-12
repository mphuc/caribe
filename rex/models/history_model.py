import datetime
from mongokit import Document
from rex import app, db
import validators

__author__ = 'taijoe'


class History(Document):
    __collection__ = 'history'

    structure = {
        'uid':  unicode,
        'user_id': unicode,
        'username': unicode,
        'fullname': unicode,
        'detail':  unicode,
        'amount': float,
        'status' :  float,
        'date_added' : datetime.datetime
    }
    use_dot_notation = True

db.register([History])