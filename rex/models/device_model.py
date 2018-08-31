import datetime
from mongokit import Document
from rex import app, db
import validators

__author__ = 'taijoe'


class Device(Document):
    __collection__ = 'device'

    structure = {
        'fullname' : unicode,
        'profit' : float,
        'address' : unicode,
        'telephone' : unicode,
        'description' : unicode,
        'status' : int,
        'date_added' : datetime.datetime,
        'date_finish' : datetime.datetime
    }
    default_values = {
        'date_added': datetime.datetime.utcnow()
        }
    use_dot_notation = True

db.register([Device])