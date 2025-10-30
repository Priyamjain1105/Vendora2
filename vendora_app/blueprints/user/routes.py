from flask import request, render_template, redirect, url_for, Blueprint



user = Blueprint('core', __name__, template_folder = 'templates')


@user.route('/')
def index():
    return render_template('core/index.html')

