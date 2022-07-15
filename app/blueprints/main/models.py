from app import db, login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key =True)
    email = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    password = db.Column(db.String(250))
    posts = db.relationship("Post", backref="user", lazy="dynamic")
    
    def hash_my_password(self, password):
        self.password = generate_password_hash(password)
            
    def check_my_password(self, password):
        return check_password_hash(self.password, password)
        

class Post(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    body = db.Column(db.String(500))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    
    def hash_my_password(self, password):
        self.password = generate_password_hash(password)
        
    def check_my_password(self, password):
        return check_password_hash(self.password, password)
    
    
class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50))
    model = db.Column(db.String(50))
    year = db.Column(db.String(50))
    color = db.Column(db.String(50))
    price = db.Column(db.Float)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)