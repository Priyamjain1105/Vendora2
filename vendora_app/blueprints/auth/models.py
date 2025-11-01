from vendora_app.app import db
from flask_login import UserMixin

class  User(db.Model, UserMixin):
      __tablename__   = 'users'
      uid = db.Column(db.Integer, primary_key = True)
      username = db.Column(db.String(100), nullable=False)
      password = db.Column(db.String(80), nullable=False)
      role = db.Column(db.String(80))
      description = db.Column(db.String(80))
      
      def __repr__ (self):
          return f'<User: {self.username}, Role: {self.role}>'
       
      # to return self uid 
      def get_id(self):
          return self.uid

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Foreign key links note to its user
    user_id = db.Column(db.Integer, db.ForeignKey('users.uid'), nullable=False)
