from flask import request, render_template, redirect, url_for, Blueprint
from vendora_app.blueprints.vendor.models import Vendor
from flask_login import login_user, logout_user, current_user, login_required

customer = Blueprint('customer', __name__, template_folder = 'templates')

@customer.route('/')
def index():
    return render_template('customer/index.html')

@customer.route('/vendors')
def vendors():
    return render_template('customer/vendors.html')
