# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from app.config import Config

# Create instances of Flask extensions
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()  # Changed the name to login_manager

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)  # Use login_manager here

    # Import and register blueprints
    from app.routes.auth import auth
    from app.routes.blog import blog
    from app.routes.user import user

    app.register_blueprint(auth)
    app.register_blueprint(blog)
    app.register_blueprint(user)

    return app





