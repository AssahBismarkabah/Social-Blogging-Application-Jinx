# app/routes/blog.py

from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required
from app import db
from app.models import BlogPost
from app.forms import BlogPostForm
from flask import Blueprint

blog = Blueprint('blog', __name__)

@blog.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = BlogPostForm()
    if form.validate_on_submit():
        # ... handle blog post creation logic ...
        return render_template('blog/create_post.html', title='New Post', form=form)
    return render_template('blog/create_post.html', title='New Post', form=form)


