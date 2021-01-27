from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, TextAreaField
from wtforms.fields.simple import TextField
from wtforms.validators import DataRequired


class LoanForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    description = TextField('description', validators=[DataRequired()])
    img = FileField('image', validators=[FileRequired()])


