# app/routes/__init__.py

from flask import Blueprint

# Import your blueprints
from app.routes.auth import auth
from app.routes.blog import blog
from app.routes.user import user_blueprint

# Register your blueprints
def register_routes(app):
    app.register_blueprint(auth)
    app.register_blueprint(blog)
    app.register_blueprint(user_blueprint)


