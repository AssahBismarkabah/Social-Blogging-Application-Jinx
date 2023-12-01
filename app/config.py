# app/config.py

import os

class Config:
    # Secret key for protecting against CSRF attacks. Change this to a secure, random value.
    SECRET_KEY = 'cr6RdeR1BVgXu+COhqhsu7cptxvkE0taMzVtwSN62Qn37+LFp8c94nl0Nd4D4rONZGiqAUWGAgwTm4HzZzO4NA=='

    # Disable Flask-SQLAlchemy modification tracking, as it can be resource-intensive.
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Enable or disable Flask debugging mode. Set to False in production.
    DEBUG = True

    # Configure the database URI based on your database choice.
    # Here, we are using SQLite as the default database. You can replace it with the URI for your chosen database.
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
    # Note: 'sqlite:///site.db' represents an SQLite database file named 'site.db' in the root directory.

    # Configure Flask-Mail for sending emails (if needed for features like password reset).
    MAIL_SERVER = 'smtp.gmail.com'  # Specify your email server
    MAIL_PORT = 587  # Port for email server
    MAIL_USE_TLS = True  # Use TLS for email transport
    MAIL_USERNAME = 'abahbismarkassah@gmail.com'  # Your email address
    MAIL_PASSWORD = 'Assah_Bismark_Abah'  # Your email password
