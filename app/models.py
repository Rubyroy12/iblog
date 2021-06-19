from app import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id= db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(20))
    email= db.Column(db.String(255))
    pass_secure= db.Column(db.String(255))


    @property
    def password(self):
            raise AttributeError('You cannot read the passwordattribute')
    @password.setter
    def password(self,password):
            self.pass_secure=generate_password_hash(password=password)

    def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)

    def __repr__(self):
            return f'User {self.username}'


class Blog(db.Model):

        """
        class blog that defines blog objects
        """
        __tablename__ = 'myblogs'
        id= db.Column(db.Integer, primary_key=True)
        title= db.Column(db.String(50))
        author= db.Column(db.String(20))
        blog= db.Column(db.String(1000))

        def save_blog(self):
                db.session.add(self)
                db.session.commit()
        @classmethod
        def get_blog(cls,id):
                blog = Blog.query.filter_by(blog_id=id).all()
                return blog
                


class Comment(db.Model):
        __tablename__ = 'comments'
        id = db.Column(db.Integer, primary_key=True)
        comment = db.Column(db.String(255))

        def save_comment(self):
                db.session.add(self)
                db.session.commit()
        @classmethod
        def get_comment(cls,id):
                comment = Comment.query.filter_by(blog_id=id).all()
                return comment
                
        def __repr__(self):
                return f'Comment: {self.comment}'
        
