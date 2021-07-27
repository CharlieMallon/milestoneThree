from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, 
    TextAreaField, BooleanField, RadioField, SelectField)
from wtforms.fields.html5 import DateField
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

# add task form
class AddTaskForm(FlaskForm):
    task_name = StringField('Title', validators=[
        InputRequired(message="Title required"), 
        Length(max=50, message="That title is too long!")])
    task_description = TextAreaField('Description and comments')
    due_date = DateField('Due Date', format='%Y-%m-%d')
    is_priority = BooleanField('Priority Task')
    is_done = BooleanField('Done!')
    task_size = RadioField('Task Size', choices=['small', 'medium', 'large'])
    task_category = SelectField('Task Category', choices=['placeholder a','placeholder b'])
    submit_button = SubmitField("Add Task")