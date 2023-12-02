# app/routes/auth.py

from flask import render_template, url_for, flash, redirect, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from app import db, bcrypt, login_manager
from app.forms import RegistrationForm, LoginForm
from app.models import User

auth = Blueprint('auth', __name__)

@auth.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # ... handle registration logic ...
        return render_template('auth/register.html', title='Register', form=form)
    return render_template('auth/register.html', title='Register', form=form)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # ... handle login logic ...
        return render_template('auth/login.html', title='Login', form=form)
    return render_template('auth/login.html', title='Login', form=form)


