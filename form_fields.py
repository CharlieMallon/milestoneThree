from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo


#Log In form
class LogInForm(FlaskForm):
    username = StringField('username', validators=[
        InputRequired(message="Username required"),
        Length(min=4, max=25, message="Username must be between 4 and 25 charactors")])
    password = PasswordField('password', validators=[
        InputRequired(message="Password required"),
        Length(min=4, max=25, message="Password must be between 4 and 25 charactors")])
    submit_button = SubmitField("Log In")

#registation form
class RegistrationForm(LogInForm):
    confirm_password = PasswordField('confirm password', validators=[
        InputRequired(message="Please confirm your password"),
        EqualTo('password', message="Passwords must match")])
    submit_button = SubmitField("Register")
