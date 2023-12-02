from flask import render_template, url_for, flash, redirect, request, Blueprint, abort
from flask_login import login_user, current_user, logout_user, login_required
from app import db, bcrypt, login_manager
from app.forms import BlogPostForm
from app.models import BlogPost
from markdown2 import markdown  # Import markdown library
from app.models import CommentForm,Comment,Notification


blog = Blueprint('blog', __name__)

@blog.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = BlogPostForm()
    if form.validate_on_submit():
        post = BlogPost(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('blog/create_post.html', title='New Post', form=form)



@blog.route("/post/<int:post_id>", methods=['GET', 'POST'])
def post_detail(post_id):
    post = BlogPost.query.get_or_404(post_id)
    html_content = markdown(post.content)

    form = CommentForm()

    if form.validate_on_submit():
        comment = Comment(content=form.content.data, author=current_user, post=post)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been added!', 'success')
        
        # Create comment notification
        post.create_comment_notification(comment)

        return redirect(url_for('blog.post_detail', post_id=post.id))

    comments = Comment.query.filter_by(post_id=post.id).all()

    return render_template('blog/post_detail.html', title=post.title, post=post, html_content=html_content, form=form, comments=comments)



@blog.route("/post/<int:post_id>/like", methods=['POST'])
@login_required
def like_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    post.like()
    flash('You liked the post!', 'success')
    
    # Create like notification
    post.create_like_notification()

    return redirect(url_for('blog.post_detail', post_id=post.id))



@blog.route("/post/<int:post_id>/share", methods=['POST'])
@login_required
def share_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    post.share()
    flash('You shared the post!', 'success')
    
    # Create share notification
    post.create_share_notification()

    return redirect(url_for('blog.post_detail', post_id=post.id))




@blog.route("/notifications")
@login_required
def notifications():
    notifications = Notification.query.filter_by(user_id=current_user.id, is_read=False).order_by(Notification.timestamp.desc()).all()

    # Mark notifications as read
    for notification in notifications:
        notification.is_read = True
    db.session.commit()

    return render_template('blog/notifications.html', title='Notifications', notifications=notifications)





@blog.route("/post/<int:post_id>/edit", methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)  # Forbidden, as user is not the author
    form = BlogPostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('blog.post_detail', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('blog/create_post.html', title='Edit Post', form=form)



@blog.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)  # Forbidden, as user is not the author
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))


