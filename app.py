import os
from flask import (Flask, render_template,
    redirect, url_for, flash, request, session, abort)
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
from datetime import datetime
from form_fields import *

if os.path.exists('env.py'):
    import env


# ---------- configure app ----------

app = Flask(__name__)

app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)

# ---------- Repeated Functions ----------
def security(user):
    
    if 'user' not in session:
        return redirect(url_for('noUser'))
    
    return user


def allTasks(user):
    """ Get all the uses tasks. Delete the tasks that are more than a day old"""

    otherTasks = list(mongo.db.tasks.find({
        'created_by': user,
        'is_priority': False, 
        'is_done': False
        }).sort('due_date', 1))

    importantTasks = list(mongo.db.tasks.find({
        'created_by': user,
        'is_priority': True,
        'is_done': False
        }).sort('due_date', 1))

    doneTasks = list(mongo.db.tasks.find({
        'created_by': user,
        'is_done': True
        }).sort('time_done', -1))

    for task in doneTasks:
        today = datetime.now().strftime('%Y-%m-%d')
        date = task['date_done']
        if date != today:
            id = task['_id']
            mongo.db.tasks.remove(id)

    return importantTasks, otherTasks, doneTasks


def progress(user):
    """ Get all the uses tasks and calculate the persentage of the progress bar 
    (number of important done task / number of done tasks + important tasks)"""

    importantTasks, otherTasks, doneTasks = allTasks(user)

    importantDoneTasks = len(list(mongo.db.tasks.find({
        'created_by': user, 
        'is_done': True, 
        'is_priority': True
        })))

    numImportantTasks = importantDoneTasks + len(importantTasks)

    lengthOtherUserTasksDone = len(list(mongo.db.tasks.find({
        'created_by': user, 
        'is_priority': False, 
        'is_done': True
        })))

    under = lengthOtherUserTasksDone + numImportantTasks

    if under == 0:
        progress = 0
    else:
        progress = round((100/(under))*(len(doneTasks)))

    progressBar = {
        'progress': progress
    }

    return progressBar


def userCategories(user):
    """Gets the user categories from the database"""

    categories_user = list(mongo.db.categories.find({
        'created_by': user
        }).sort('category_name', 1))

    return categories_user


def categories(user):
    """Gets the all the categories from the database"""

    categories_admin = list(mongo.db.categories.find({'created_by': 'admin'}))
    categories_user = userCategories(user)

    categories = (*categories_admin, *categories_user)

    category_names = [(category['category_name']) for category in categories]
    category_names.sort()
    return category_names


def addCategory(cat_name, user):
    """If the task category exists, find it on the database, if not create a new user category."""
    existing_cat = mongo.db.categories.find_one(
        {'category_name': cat_name})
    if not existing_cat:
        category = {
            'category_name' : cat_name,
            'created_by': user
            }
        mongo.db.categories.insert_one(category)
        flash('New Category Added')


def findOneCat(category_id):
    try:
        category = mongo.db.categories.find_one_or_404({
            '_id': ObjectId(category_id)})
        return category
    except:
        abort(404)


def findOneTask(task_id):
    try:
        task = mongo.db.tasks.find_one_or_404({
            '_id': ObjectId(task_id)})
        return task
    except:
        abort(404)


def authorised(user, item):
    if item['created_by'] == user:
        return item
    abort(403)


# ---------- load pages - no security required ----------
@app.route('/')
def noUser():
    """Puts no user in session for the home page"""

    session['user'] = 'no'
    return render_template('home.html')

@app.route('/register', methods=[ 'GET', 'POST'])
def register():
    """Checks if user exists if it doesn't adds to the database"""

    form = RegistrationForm()

    if request.method == 'POST' and form.validate_on_submit():
        existing_user = mongo.db.users.find_one(
            {'username': form.username.data.lower()})

        if existing_user:
            flash('Username already exists')
            return redirect(url_for('register'))

        register = {
            'username': form.username.data.lower(),
            'password': generate_password_hash(form.password.data)
            }
        mongo.db.users.insert_one(register)

        session['user'] = form.username.data.lower()
        flash('Registration Successful!')

        return render_template('account.html', username=session['user'])

    return render_template('register.html', form=form)


@app.route('/login', methods=[ 'GET', 'POST'])
def login():
    """Checks if user exists and the password provided matches the one on
    the database, if it matches return account page if not display an error"""

    form = LogInForm()

    if request.method == 'POST':

        existing_user = mongo.db.users.find_one(
            {'username': form.username.data.lower()})

        if existing_user:

            if check_password_hash(
                existing_user['password'], form.password.data):
                    session['user'] = form.username.data.lower()

                    return redirect(url_for(
                        'account', username=session['user']))
            else:

                flash('Incorrect Username and/or Password')
                return redirect(url_for('login'))
        else:

                flash('Incorrect Username and/or Password')
                return redirect(url_for('login'))

    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    """Remove user from session cookies"""
    session.pop('user')
    session['user'] = 'no'
    return redirect(url_for('home'))


@app.route('/contact')
def contact():
    """load the contact page"""
    progressBar = progress(session['user'])

    return render_template('contact.html', progressBar=progressBar)


# ---------- load pages - Security ----------
@app.route('/home')
def home():
    """When there is a user logged in, display the Users Tasks"""

    form = DeleteForm()
    user = security(session['user'])

    importantTasks, otherTasks, doneTasks = allTasks(user)
    progressBar = progress(user)

    tasks = (importantTasks + otherTasks + doneTasks)
    toDo = (importantTasks + otherTasks)
    
    return render_template('home.html', tasks=tasks, doneTasks=doneTasks, toDo=toDo,
        progressBar=progressBar, form=form)


@app.route('/account/<username>')
def account(username):
    """When there is a user logged in, display the Users Tasks and Categories"""

    user = security(session['user'])
    form = DeleteForm()

    if user != username:
        return redirect(url_for('login'))

    categories = userCategories(username)
    importantTasks, otherTasks, doneTasks = allTasks(username)
    progressBar = progress(username)

    return render_template('account.html', username=user, 
        categories=categories, importantTasks=importantTasks, 
        otherTasks=otherTasks, doneTasks=doneTasks, 
        progressBar=progressBar, form=form)


@app.route('/edit_categories/<category_id>', methods=['GET', 'POST'])
def edit_category(category_id):
    """Gets one of the user categories puts it on the page, updates the 
    database with the editted category"""

    user = security(session['user'])

    progressBar = progress(user)
    form = EditCategoryForm()
    item = findOneCat(category_id)
    category = authorised(user, item)

    if request.method == 'POST':
        submit = {
            'category_name': form.task_category.data,
            'created_by': user
        }
        mongo.db.categories.update({'_id': category['_id']},submit)
        flash('Task Successfully Updated')
        return redirect(url_for('account', username=user))
    elif request.method == 'GET':
        form.task_category.data = category['category_name']
    else:
        abort(404)

    return render_template('edit_category.html', category=category, 
        form=form, progressBar=progressBar)


@app.route('/delete_category/<category_id>', methods=['GET', 'POST'])
def delete_category(category_id):
    """Gets the categories by ID and deletes the category"""

    security(session['user'])

    category = findOneCat(category_id)
    form = DeleteForm()
    user = security(session['user'])

    item = findOneCat(category_id)
    category = authorised(user, item)

    if request.method == 'POST':
        if form.submit_button.data:
            mongo.db.categories.remove({'_id': category['_id']})
            flash('Category Successfully Deleted')
        return redirect(request.referrer)
    else:
        abort(404)


@app.route('/add_task', methods=[ 'GET', 'POST'])
def add_task():
    """Finds all the categories and populates them on the site.
    Gets the new task and adds it to the database. Select or create task category.
    If no task details given then fill in with an empty string"""

    user = security(session['user'])

    form = AddTaskForm()
    category_names = categories(user)
    progressBar = progress(user)

    form.task_category.choices = category_names

    if request.method == 'POST':

        if form.add_category.data != '':
            cat_name = form.add_category.data.capitalize()
            addCategory(cat_name, user)
        else:
            cat_name = form.task_category.data.capitalize()

        task = {
            'task_name': form.task_name.data.capitalize(),
            'task_description': form.task_description.data,
            'due_date': str(form.due_date.data),
            'is_priority': form.is_priority.data,
            'is_done': form.is_done.data,
            'task_size': form.task_size.data,
            'category_name': cat_name,
            'created_by': user
        }

        mongo.db.tasks.insert_one(task)
        flash('Task Successfully Added')
        return redirect(url_for('home'))

    return render_template('add_task.html', form=form, 
        progressBar=progressBar)


@app.route('/edit_task/<task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    """Gets one of the user tasks by ID puts it on the page, updates the 
    database with the editted task. Select or create task category. 
    If no task details given then fill in with an empty string"""

    user = security(session['user'])

    item = findOneTask(task_id)
    task = authorised(user, item)

    form = EditTaskForm()
    category_names = categories(user)
    progressBar = progress(user)

    form.task_category.choices = category_names

    if request.method == 'POST':
        if form.add_category.data != '':
            cat_name = form.add_category.data.capitalize()
            addCategory(cat_name, user)
        else:
            cat_name = form.task_category.data.capitalize()

        submit = {
            'task_name': form.task_name.data.capitalize(),
            'task_description': form.task_description.data,
            'due_date': str(form.due_date.data),
            'is_priority': form.is_priority.data,
            'is_done': form.is_done.data,
            'task_size': form.task_size.data,
            'category_name': cat_name,
            'created_by': user
        }

        mongo.db.tasks.update({'_id': ObjectId(task_id)},submit)
        flash('Task Successfully Updated')
        return redirect(url_for('home'))

    elif request.method == 'GET':
        if task['due_date'] != 'None':
            due_date = datetime.strptime(task['due_date'], '%Y-%m-%d')
        else:
            due_date = ''

        form.task_name.data = task['task_name']
        form.task_description.data = task['task_description']
        form.due_date.data = due_date
        form.is_priority.data = task['is_priority']
        form.is_done.data = task['is_done']
        form.task_size.data = task['task_size']
        form.task_category.data = task['category_name']

    else:
        return redirect(url_for('not_found'))

    return render_template('edit_task.html', task=task, form=form, 
        categories=categories, progressBar=progressBar)


@app.route('/delete_task/<task_id>', methods=['GET', 'POST'])
def delete_task(task_id):
    """Gets the task by ID and deletes the task"""

    task = findOneTask(task_id)
    form = DeleteForm()
    user = security(session['user'])

    item = findOneTask(task_id)
    task = authorised(user, item)

    if request.method == 'POST':
        if form.submit_button.data:
            mongo.db.tasks.remove({'_id': task['_id']})
            flash('Task Successfully Deleted')
        return redirect(request.referrer)
    else:
        abort(404)


@app.route('/done_task/<task_id>', methods=['GET', 'POST'])
def done_task(task_id):
    """Gets the task by ID and toggles the done state"""

    security(session['user'])

    # post methord here

    task = findOneTask(task_id)

    if task['is_done'] == True :
        done = {
        'task_name': task['task_name'],
        'task_description': task['task_description'],
        'due_date': task['due_date'],
        'is_priority': task['is_priority'],
        'task_size': task['task_size'],
        'category_name': task['category_name'],
        'created_by': task['created_by'],
        'is_done': not task['is_done'],
        'date_done': 'none',
        'time_done': 'none'
        }
        status = 'Task Successfully Un-done'
    else:
        done = {
        'task_name': task['task_name'],
        'task_description': task['task_description'],
        'due_date': task['due_date'],
        'is_priority': task['is_priority'],
        'task_size': task['task_size'],
        'category_name': task['category_name'],
        'created_by': task['created_by'],
        'is_done': not task['is_done'],
        'date_done': datetime.now().strftime('%Y-%m-%d'),
        'time_done': datetime.now()
        }
        status = 'Task Successfully Done'

    mongo.db.tasks.update({'_id': ObjectId(task_id)},done)
    flash(status)
    return redirect(request.referrer)


@app.route('/priority_task/<task_id>', methods=['GET', 'POST'])
def priority_task(task_id):
    """Gets the task by ID and toggles the priority state"""

    security(session['user'])

    # post methord here

    task = findOneTask(task_id)

    priority = {
        'task_name': task['task_name'],
        'task_description': task['task_description'],
        'due_date': task['due_date'],
        'is_priority': not task['is_priority'],
        'task_size': task['task_size'],
        'category_name': task['category_name'],
        'created_by': task['created_by'],
        'is_done': task['is_done'],
    }

    if task['is_priority'] == True :
        status = 'Task Successfully Un-prioritised'
    else:
        status = 'Task Successfully prioritised'

    mongo.db.tasks.update({'_id': ObjectId(task_id)},priority)
    flash(status)

    return redirect(request.referrer)


# error handling
@app.errorhandler(500) 
@app.errorhandler(404)
def not_found(error): 
    """Load error Page"""
    progressBar = progress(session['user'])
    return render_template('error.html', progressBar=progressBar)

@app.errorhandler(403)
@app.errorhandler(405)
def access_denied(error): 
    """Load error Page"""
    progressBar = progress(session['user'])
    return render_template('denied.html', progressBar=progressBar)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=os.environ.get('DEVELOPMENT')),
