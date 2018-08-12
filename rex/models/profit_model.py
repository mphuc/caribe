import datetime
from mongokit import Document
from rex import app, db
import validators

__author__ = 'taijoe'


class Profit(Document):
    __collection__ = 'profit'

    structure = {
        'uid' : unicode,
        'username' : unicode,
        'fullname' : unicode,
        'account_horder' : unicode,
        'account_number' : unicode,
        'bankname' : unicode,
        'brandname' : unicode,
        'amount': float,
        'date_added' : datetime.datetime,
        'status' : int,
        'telephone' : unicode
    }
    use_dot_notation = True

db.register([Profit])