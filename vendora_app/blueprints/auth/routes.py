from flask import request, render_template, redirect, url_for, Blueprint, session
from vendora_app.app import db, bcrypt

from flask_login import login_user, logout_user, current_user, login_required
from vendora_app.blueprints.auth.models import User, Note


auth = Blueprint('auth', __name__, template_folder = 'templates')





"""
@auth.route('/')
def index():
    todos = User.query.all()
    return render_template('todos/index.html' , todos = todos)


@auth.route('/create', methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('todos/create.html')
    elif request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        done = True if 'done' in request.form.keys() else False
        
        description = description if description != ''else None
        todo = Todo(title= title, description=description, done = done)
        
        db.session.add(todo)
        db.session.commit()
        
        return redirect(url_for('todos.index'))
"""
    
@auth.route('/')
def index():
    return render_template('auth/index.html')

@auth.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'GET':
        return render_template('auth/signup.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        hashed_password = bcrypt.generate_password_hash(password)
        user = User(username =username, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        
        user = User.query.filter(User.username == username).first()
        
        if bcrypt.check_password_hash(user.password,password):
            login_user(user)
            return redirect(url_for('customer.vendors'))
        else:
            return 'Failed'
        
        
        #return redirect(url_for('auth.login'))

@auth.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('auth/login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        
        user = User.query.filter(User.username == username).first()
        
        if bcrypt.check_password_hash(user.password,password):
            login_user(user)
            return redirect(url_for('customer.vendors'))
        else:
            return 'Failed'

@auth.route('/logout')
def logout():
    logout_user()
    session.clear()
    return redirect(url_for('customer.vendors'))

@auth.route('/new_note',methods = ['GET','POST'])
@login_required
def new_note():
    if request.method == 'GET':
        return render_template('auth/note.html')
    elif request.method == 'POST':
        print("got request")
        note = request.form.get('note')
        new_note = Note(content=note, user_id=current_user.uid)
        db.session.add(new_note)
        db.session.commit()
        #flash('Note added successfully!', 'success')
        return redirect(url_for('auth.show_notes'))
        
@auth.route("/show_notes")
def show_notes():
        user_notes = Note.query.filter_by(user_id=current_user.uid).all()
        notes_html = "<ul>"
        for n in user_notes:
            notes_html += f"<li>{n.content}</li>"
        notes_html += "</ul>"

        return f"""
            <a href="/">Home</a> 

            <a href="/logout">logout</a>
            <p>Note added successfully!</p>
            {notes_html}
            <a href="/new_note">Add another note</a> <br>
            
            
            
        """