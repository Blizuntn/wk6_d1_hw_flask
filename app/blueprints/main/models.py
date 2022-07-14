from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    email = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    password = db.Column(db.String(50))
    posts = db.relationship("Post", backref="user", lazy="dynamic")

class Post(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    body = db.Column(db.String(500))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    
    
class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50))
    model = db.Column(db.String(50))
    year = db.Column(db.String(50))
    color = db.Column(db.String(50))
    price = db.Column(db.Float)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))