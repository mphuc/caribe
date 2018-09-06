import datetime
from mongokit import Document
from rex import app, db
import validators
from bson.objectid import ObjectId
__author__ = 'taijoe'


class User(Document):
    __collection__ = 'users'

    structure = {
        'name': unicode,
        
        'customer_id' : unicode,
        'email': unicode,
        'username': unicode,
        'password': unicode,
        
        'creation': datetime.datetime,
        'p_binary' : unicode,
        'left' : unicode,
        'right' : unicode,
        'level_thuongthem' : float,
        'telephone' : float,
        'p_node' : unicode,
        'password_transaction' : unicode,
        'cmnd' : unicode,
        'birthday' : unicode,
        'account_horder' : unicode,
        'account_number' : unicode,
        'bankname' : unicode,
        'brandname' : unicode,
        
        'level' : int,
        'password_custom' : unicode,
        
        'total_left' : float,
        'total_right' : float,
        'count_left' : float,
        'count_right': float,
        'count_lefts' : float,
        'count_rights': float,
        'count_leftss' : float,
        'count_rightss': float,
        'm_wallet' : float,
        'r_wallet' : float,
        's_wallet' : float,
        't_wallet' : float,
        'g_wallet' : float,
        'daily_wallet' : float,
        'cancap_wallet' : float,
        'tructiep_wallet' :  float,
        'thunhapf1_wallet' :  float,
        'thuetncn_wallet' :  float,
        'tichluy_wallet' :  float,
        'status_authen' : int,
        'authentication' : unicode,
        'total_receive' : float,
        'position' : unicode,
        'country' : unicode,
        'total_invest' : float,
        'roi' : float,
        'max_binary' : float,
        'code_active': unicode,
        'address' : unicode,
        'status':int,
        'status_re':int,
        'type': int,
        'total_commission': float,
        'secret_2fa': unicode,
        'status_2fa': int,
        'status_withdraw' : int,
        'max_daily': float,
        'current_max_daily': float,
        's_left': float,
        's_right': float,
        's_p_node': float,
        's_p_binary': float,
        's_token': float,
        'total_node': float,
        'active' : int
    }
    validators = {
        'name': validators.max_length(50),
        'email': validators.max_length(120)
    }
    default_values = {
        'creation': datetime.datetime.utcnow(),
        'm_wallet' : 0,
        'r_wallet' : 0,
        's_wallet' : 0,
        't_wallet' : 0,
        'g_wallet' : 0,
        'level_thuongthem' : 0,
        'total_receive' : 0,
        'total_left' : 0,
        'total_right' : 0,
        'count_left' : 0,
        'count_rights' : 0,
        'count_lefts' : 0,
        'count_right' : 0,
        'count_rightss' : 0,
        'count_leftss' : 0,
        'level' : 0,
        'status_authen' : 0,
        'active' : 0,
        'thunhapf1_wallet' : 0,
        'authentication' : '',
        'left' : '',
        'right' : '',
        'p_binary' : '',
        'type': 0,
        'status_re' :0,
        'total_node' : 0,
        'daily_wallet' : 0,
        'cancap_wallet' : 0,
        'tructiep_wallet' : 0,
        'thuetncn_wallet' :  0,
        'tichluy_wallet' :  0

        }
    use_dot_notation = True

    def __repr__(self):
        return '<User %r>' % self.name

    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self._id

    def get_role(self):
        return self.role

    def get_user_home(self):
        role = db['roles'].find_one({'_id': self.get_role()})
        return role['home_page']


db.register([User])