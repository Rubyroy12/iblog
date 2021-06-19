from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import required

class BlogForm(FlaskForm):
    title = StringField('Blog title', validators=[required()])
    author = StringField('Author')
    blog = TextAreaField('Blog')
    submit =SubmitField('Submit')