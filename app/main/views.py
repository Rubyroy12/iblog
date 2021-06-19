from . import main
from flask import render_template,redirect, url_for,abort,flash
from flask_login import login_required, current_user
from ..models import Blog,User,Comment
from .forms import BlogForm,CommentsForm,SubscriptionForm
from .. import db
import markdown2 
# from ..email import mail_message

@main.route('/')
def index():

    return render_template('index.html' , current_user=current_user)


@main.route('/blogs')
def blog():
    # user = User.query.filter_by(username = uname).first()

    all_blogs=Blog.query.order_by(Blog.title).all()

    return render_template("blogs.html", blogs=all_blogs)

@main.route('/blogs/makeblog',methods=['POST','GET'])
def create():

    form = BlogForm()
   
    if form.validate_on_submit():
        title = form.title.data
        blog= form.blog.data
        author = form.author.data
        
        new_blog = Blog(title=title,blog=blog, author=author)
        new_blog.save_blog()
        db.session.add(new_blog)
        db.session.commit()
        return redirect(url_for('main.blog'))
      
    
    
    return render_template("makeblog.html", blog_form=form)

@main.route('/comments/<int:id>',methods=['POST','GET'])
def comments(id):
    blog = Blog.query.get(id)
    commentform = CommentsForm()
    subscribe = SubscriptionForm()
    if commentform.validate_on_submit():
        comment= commentform.comment.data
        new_comment=Comment(comment=comment)
        new_comment.save_comment()
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('main.comments',id = id))
    
    if subscribe.validate_on_submit():
        email = subscribe.email.data
        new_subscriber=Subscribe(email=email)
        new_subscriber.save_email()
        db.session.add(new_subscriber)
        db.session.commit()
        return redirect(url_for('main.comments',id= id))
    
    flash('Thank you for subscribing to our Blog!!')
    comment = Comment.query.filter_by(id=id).all()
    format_blog = markdown2.markdown(blog.blog,extras=["code-friendly", "fenced-code-blocks"])
    return  render_template("comments.html", blog=blog, format_blog=format_blog , commentform=commentform, comments=comment)

