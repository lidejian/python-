from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class CommentForm(FlaskForm):
    name = StringField('name')
    comment = TextAreaField ('comment', validators=[DataRequired()])

class FindForm(FlaskForm):
    name = StringField('name')