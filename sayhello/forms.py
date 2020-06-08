#encoding:utf-8
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,FloatField,SelectField,RadioField
from wtforms.validators import  DataRequired,Length

class HelloForm(FlaskForm):
    Card_Id=StringField("Your Bank Card Number",validators=[DataRequired()])
    Age=FloatField("Age", validators=[DataRequired()])
    Income=FloatField("Salary", validators=[DataRequired()])
    Height = FloatField("Height", validators=[DataRequired()])
    Weight=FloatField("Weight",validators=[DataRequired()])
    Marriage = SelectField('Marriage', choices=[('Married', 'Married'), ('Unmarried', 'Unmarried'), ("Divorced", "Divorced")], validators=[DataRequired()])
    Sex = SelectField('Sex', choices=[('Male','Male'), ('Female','Female'),("Unknown","Unknown")], validators=[DataRequired()])
    submit=SubmitField()
