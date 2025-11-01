from flask import request, render_template, redirect, url_for, Blueprint



core = Blueprint('core', __name__, template_folder = 'templates')


@core.route('/')
def index():
    #return render_template('vendor/index.html')
    return redirect(url_for('vendor.index'))

@core.route('/about')
def about():
    return render_template('core/index.html')

@core.route('/developer')
def developer():
    routes = [
        {"name": "Home", "path": "/", "url": url_for('core.index'), "status": "Completed"},
        {"name": "Vendor Dashboard", "path": "/vendor/dashboard", "url": url_for('vendor.dashboard'), "status": "In Progress"},
        {"name": "Customer Page", "path": "/customer/index", "url": url_for('customer.index'), "status": "In Progress"},
        {"name": "Appointments", "path": "/vendor/appointments", "url": url_for('vendor.appointments'), "status": "Not Started"},
        {"name": "Analytics", "path": "/vendor/analytics", "url": url_for('vendor.analytics'), "status": "Not Started"},
        {"name": "Support Page", "path": "/vendor/support", "url": url_for('vendor.support'), "status": "Not Started"},
        
        # ➕ Just add new ones here ↓
        # {"name": "New Page", "path": "/new", "url": url_for('new_page'), "status": "In Progress"},
    ]
    #return render_template('developer_page.html', routes=routes)
    return render_template('core/developer_page.html',routes=routes)
