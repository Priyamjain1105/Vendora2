from flask import request, render_template, redirect, url_for, Blueprint
from vendora_app.blueprints.vendor.models import Vendor
from flask_login import login_user, logout_user, current_user, login_required

vendor = Blueprint('vendor', __name__, template_folder = 'templates')

@vendor.route('/')
def index():
    return render_template('vendor/index.html')

