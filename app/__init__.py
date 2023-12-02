# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_social import Social  # Import Flask-Social
from app.config import Config

# Create instances of Flask extensions
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
bcrypt = Bcrypt()
social = Social()  # Create an instance of Flask-Social

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    social.init_app(app)  # Initialize Flask-Social

    # Import and register blueprints
    from app.routes.auth import auth
    from app.routes.blog import blog
    from app.routes.user import user_blueprint

    app.register_blueprint(auth)
    app.register_blueprint(blog)
    app.register_blueprint(user_blueprint)

    return app








