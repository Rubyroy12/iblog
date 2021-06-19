from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import required,Email

class BlogForm(FlaskForm):
    title = StringField('Blog title', validators=[required()])
    author = StringField('Author')
    blog = TextAreaField('Blog')
    submit =SubmitField('Submit')

class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[required()])
    submit = SubmitField('Submit')
class SubscriptionForm(FlaskForm):
    email = StringField('Your Email Address',validators=[required(),Email()])
    submit = SubmitField('Subscribe')
