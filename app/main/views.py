from . import main
from flask import render_template,redirect, url_for,abort
from flask_login import login_required, current_user
from ..models import Blog,User
from .forms import BlogForm
from .. import db

@main.route('/')
def index():

    return render_template('index.html' , current_user=current_user)


@main.route('/blogs')
def blog():
    # user = User.query.filter_by(username = uname).first()

    
    return render_template("blogs.html")

@main.route('/blogs/makeblog')
def create():

    form = BlogForm()
   
    if form.validate_on_submit():
        title = form.title.data
        blog= form.blog.data
        author = form.author.data
        
        new_blog = Blog(title=title,blog=blog, author=author)
        new_blog.save_blog()
        return redirect(url_for('main.blog'))
    
    
    return render_template("makeblog.html", blog_form=form)

