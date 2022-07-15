from app.blueprints.auth.routes import login
from flask import render_template, redirect, url_for
from . import bp as app
from app.blueprints.main.models import Car
from flask_login import login_required, current_user

@app.route("/")
# @login_required
def home():
    
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    
    cars = Car.query.all()
    
    cars.sort(key=lambda post: post.date_created, reverse= True)
    print(cars)
    context ={
        "cars":cars,
    }
    return render_template("index.html", **context)

@app.route("/about")
def about():
    return render_template("about.html")