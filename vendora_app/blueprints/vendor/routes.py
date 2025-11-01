from flask import request, render_template, redirect, url_for, Blueprint
from vendora_app.blueprints.vendor.models import Vendor
from flask_login import login_user, logout_user, current_user, login_required

vendor = Blueprint('vendor', __name__, template_folder = 'templates')

@vendor.route('/')
def index():
    return render_template('vendor/index.html')

@vendor.route('/dashboard')
def dashboard():
    return render_template('vendor/dashboard.html')

@vendor.route('/edit_business')
def edit_business():
    return render_template('vendor/dashboard.html')

@vendor.route('/appointments')
def appointments():
    return render_template('vendor/dashboard.html')

@vendor.route('/analytics')
def analytics():
    return render_template('vendor/dashboard.html')

@vendor.route('/reviews')
def reviews():
    return render_template('vendor/dashboard.html')

@vendor.route('/support')
def support():
    return render_template('vendor/dashboard.html')