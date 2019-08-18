from wtforms import Form 
from wtforms import FloatField
from wtforms import validators
from wtforms.validators import DataRequired

class Flower_Form(Form):
	LS = FloatField('LS', validators=[DataRequired()])
	AS = FloatField('AP', validators=[DataRequired()])
	LP = FloatField('LP', validators=[DataRequired()])
	AP = FloatField('AP', validators=[DataRequired()])