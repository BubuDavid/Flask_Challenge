from wtforms import Form 
from wtforms import StringField, TextField, IntegerField
from wtforms.fields.html5 import EmailField 
from wtforms import validators
from wtforms.validators import DataRequired

class CommentForm(Form):
	parametros1 = IntegerField('parámetro 1', validators=[DataRequired()])
	parametros2 = IntegerField('parámetro 2', validators=[DataRequired()])
	parametros3 = IntegerField('parámetro 3', validators=[DataRequired()])
	parametros4 = IntegerField('parámetro 4', validators=[DataRequired()])