from flask import render_template,request,redirect,url_for,abort,flash
from . import blogs
from flask_login import login_required,current_user
from ..models import User,Blog,Comment
from .forms import PostForm ,CommentForm
from .. import db

#Create a blog
@blogs.route('/create',methods = ['GET','POST'])
@login_required
def create_post():
    post_form = PostForm()
    if post_form.validate_on_submit():
        post = Blog(title = post_form.title.data,
                    body = post_form.body.data,
                    user_id = current_user.id)
        db.session.add(post)
        db.session.commit()
        flash('Post saved')
        return redirect(url_for('main.index'))
    return render_template('blog/create_post.html', post_form=post_form)

# VIEW A POST
@blogs.route('blog/<int:post_id>')
def post(post_id):
    post = Blog.query.get_or_404(post_id)
    return render_template('blog/post.html', title =post.title, date = post.posted, post = post)
