from flask import Blueprint, request, session, redirect, url_for, render_template
from flask.ext.login import login_user, logout_user, current_user, login_required
from rex import app, db
from rex.models import user_model, deposit_model, history_model, invoice_model

__author__ = 'carlozamagni'

history_ctrl = Blueprint('history', __name__, static_folder='static', template_folder='templates')


@history_ctrl.route('/history', methods=['GET', 'POST'])
def history():
	if session.get(u'logged_in') is None:
		return redirect('/user/login')
	uid = session.get('uid')
	query = db.historys.find({'uid': uid})
	user = db.User.find_one({'customer_id': uid})
	data ={
		'history' : query,
		'title': 'History',
		'menu' : 'history',
		'user': user
		
	}
	return render_template('account/history.html', data=data)

