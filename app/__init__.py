# app/__init__.p
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config

# Create instances of Flask extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Import and register blueprints
    from app.routes.auth import auth_blueprint
    from app.routes.blog import blog_blueprint
    from app.routes.user import user_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(blog_blueprint)
    app.register_blueprint(user_blueprint)

    return app


