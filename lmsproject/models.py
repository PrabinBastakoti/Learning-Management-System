from lmsproject import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), nullable= False)
    lastname = db.Column(db.String(20), nullable= False)
    email = db.Column(db.String(100),unique=True,nullable=False)
    image_file = db.Column(db.String(20),nullable=False,default= 'user.png')
    phonenumber = db.Column(db.String(20),unique=True,nullable=False)
    password = db.Column(db.String(60),nullable= False)
    birthdate = db.Column(db.String(20),nullable=False)
    gender = db.Column(db.String(20),nullable=False)
    address = db.Column(db.String(30),nullable=False)
    university = db.Column(db.String(50),nullable=False)
    college = db.Column(db.String(50),nullable=True)
    regnum = db.Column(db.String(20),nullable=True)

    posts = db.relationship('Post',backref='author',lazy=True)

    def __repr__(self):
        return f"User('{self.firstname}','{self.lastname}','{self.email}','{self.image_file}')"

    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100),nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text,nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"