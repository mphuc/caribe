import datetime
from mongokit import Document
from rex import app, db
import validators

__author__ = 'taijoe'


class Deposit(Document):
    __collection__ = 'deposit'

    structure = {
        'uid' : unicode,
        'username' : unicode,
        'fullname' : unicode,
        'amount' : float,
        'monthly' : float,
        'status' : int,
        'date_added' : datetime.datetime,
        'date_finish' : datetime.datetime
    }
    default_values = {
        'date_added': datetime.datetime.utcnow()
        }
    use_dot_notation = True

db.register([Deposit])