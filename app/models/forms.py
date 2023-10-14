from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password= PasswordField("password", validators=[DataRequired()])

class RegisterForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password= PasswordField("password", validators=[DataRequired()])
    name= StringField("name", validators=[DataRequired()])
    email= StringField("email", validators=[DataRequired()])
    cargo = StringField("cargo",validators=[DataRequired()])
    area = StringField("area",validators=[DataRequired()])

class SkapForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    area = StringField("area", validators=[DataRequired()])
    turno = StringField("turno", validators=[DataRequired()])
    number_id = IntegerField("number_id", validators=[DataRequired()])
    q1 = IntegerField("q1", validators=[DataRequired()])
    q2 = IntegerField("q2", validators=[DataRequired()])
    q3 = IntegerField("q3", validators=[DataRequired()])
    q4 = IntegerField("q4", validators=[DataRequired()])
    