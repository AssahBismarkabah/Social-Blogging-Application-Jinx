# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt  # Import Bcrypt
from app.config import Config

# Create instances of Flask extensions
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()  # Changed the name to login_manager
bcrypt = Bcrypt()  # Create an instance of Bcrypt

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bcrypt.init_app(app)  # Initialize Bcrypt

    # Import and register blueprints
    from app.routes.auth import auth
    from app.routes.blog import blog
    from app.routes.user import user_blueprint  # Correct import name

    app.register_blueprint(auth)
    app.register_blueprint(blog)
    app.register_blueprint(user_blueprint)  # Correct blueprint name

    return app







