from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    
    
    @app.route("/")
    def home():
        return render_template("index.html")
    
    @app.route("/about")
    def about():
        return render_template("about.html")
    
    @app.route("/register")
    def register():
        return render_template("register.html")
    
    @app.route("/login")
    def login():
        return render_template("login.html")
    
    @app.route("/blog")
    def blog():
        return render_template("blog.html")
    
    return app