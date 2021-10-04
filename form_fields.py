from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField,
                     TextAreaField, BooleanField, RadioField, SelectField)
from wtforms.fields.html5 import DateField
from wtforms.validators import InputRequired, Length, EqualTo


# Log In form
class LogInForm(FlaskForm):
    username = StringField('Username', validators=[
        InputRequired(message="Username required"),
        Length(min=4, max=10,
               message="Username must be between 4 and 10 characters")])
    password = PasswordField('Password', validators=[
        InputRequired(message="Password required"),
        Length(min=4, max=25,
               message="Password must be between 4 and 25 characters")])
    submit_button = SubmitField("Log In")
    cancel_button = SubmitField("Cancel", render_kw={'formnovalidate': True})

# registation form


class RegistrationForm(LogInForm):
    confirm_password = PasswordField('Confirm Password', validators=[
        InputRequired(message="Please confirm your password"),
        EqualTo('password', message="Passwords must match")])
    submit_button = SubmitField("Register")
    cancel_button = SubmitField("Cancel", render_kw={'formnovalidate': True})

# add task form


class AddTaskForm(FlaskForm):
    task_name = StringField('Task Title', validators=[
        InputRequired(message="Title required"),
        Length(max=50, message="That title is too long!")])
    task_description = TextAreaField('Description')
    due_date = DateField('Due Date', format='%Y-%m-%d')
    is_priority = BooleanField('Prioritize Task')
    is_done = BooleanField('Done!')
    task_size = RadioField('Task Size',
                           choices=['small', 'medium', 'large'], default='small')
    task_category = SelectField('Task Category')
    add_category = StringField('Task Category', validators=[
        Length(min=4, max=20,
               message="Category must be between 4 and 20 characters")])
    submit_button = SubmitField("Add Task")
    cancel_button = SubmitField("Cancel", render_kw={'formnovalidate': True})

# Edit Task form


class EditTaskForm(AddTaskForm):
    submit_button = SubmitField("Edit Task")
    cancel_button = SubmitField("Cancel", render_kw={'formnovalidate': True})

# Edit Category form


class EditCategoryForm(FlaskForm):
    task_category = StringField('Task Category', validators=[
        Length(min=4, max=17,
               message="Category must be between 4 and 20 characters")])
    submit_button = SubmitField("Edit Category")
    cancel_button = SubmitField("Cancel", render_kw={'formnovalidate': True})

# Delete form


class DeleteForm(FlaskForm):
    submit_button = SubmitField("Yes")
    cancel_button = SubmitField("No", render_kw={'formnovalidate': True})
