from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

with open('example.sql', 'r') as file:
    data = file.read()

class CodeForm(FlaskForm):
    code = TextAreaField('Enter code here:', validators=[DataRequired()], default=data)
    run = SubmitField('Run')