from flask import Flask, jsonify, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)
    
    migrate = Migrate()
    
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    
    from app.blueprints.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    from app.blueprints.api import bp as api_bp
    app.register_blueprint(api_bp)
    
    from app.blueprints.auth import bp as auth_bp
    app.register_blueprint(auth_bp)
    
    
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