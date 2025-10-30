from flask import request, render_template, redirect, url_for, Blueprint



vendor = Blueprint('core', __name__, template_folder = 'templates')


@vendor.route('/')
def index():
    return render_template('core/index.html')

