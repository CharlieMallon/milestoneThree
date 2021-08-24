import os
from flask import (Flask, render_template,
    redirect, url_for, flash, request, session)
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
from datetime import datetime
from form_fields import *

if os.path.exists("env.py"):
    import env


# configure app
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    # See if there is a user logged in
    try:
        # If there is pop them in the session user
        if session["user"]:
            session["user"] = session["user"]
    except:
        # If not make the session user none
        # change this to something shorter
        session["user"] = 'none'

    # ---------- All Task contents ----------
    # Gets the other tasks and orders them by date
    otherUserTasks = list(mongo.db.tasks.find({
        "created_by": session["user"],
        "is_priority": False, 
        "is_done": False
        }).sort("due_date", 1))

    # ---------- Task and Progress Bar contents ----------
    # Gets the important tasks and orders them by date
    importantUserTasks = list(mongo.db.tasks.find({
        "created_by": session["user"],
        "is_priority": True,
        "is_done": False
        }).sort("due_date", 1))
    # Gets the done tasks and orders them by date/time done
    doneTasks = list(mongo.db.tasks.find({
        "created_by": session["user"],
        "is_done": True
        }).sort("date_done", -1))

    # ---------- Progress Bar contents ----------
    # Gets the number of important tasks that have been done
    importantDoneTasks = len(list(mongo.db.tasks.find({
        "created_by": session["user"], 
        "is_done": True, 
        "is_priority": True
        })))
    # Number of Important tasks (done + not Done)
    numImportantTasks = importantDoneTasks + len(importantUserTasks)
    # Number of tasks done that are not important
    lengthOtherUserTasksDone = len(list(mongo.db.tasks.find({
        "created_by": session["user"], 
        "is_priority": False, 
        "is_done": True
        })))
    # Number of Tasks that make up the task bar 
    under = lengthOtherUserTasksDone + numImportantTasks
    
    # ---------- Progress Bar ----------
    # Fill of the Task Bar
    if under == 0:
        progress = 0
    else:
        progress = (100/(under))*(len(doneTasks))
    # Puts the progress in a dictionary
    progressBar = {
        "progress": progress
    }

    # ---------- All Task ----------
    # Get all the tasks and put them in order
    tasks = (importantUserTasks + otherUserTasks + doneTasks)
    
    # When the Get methord is called load the page with all the users
    # tasks on it
    return render_template("home.html", tasks=tasks, 
        progressBar=progressBar)


@app.route("/register", methods=[ 'GET', 'POST'])
def register():
    # Set up the form
    form = RegistrationForm()

    # When the Post methord is called and the form is valid.
    if request.method == "POST" and form.validate_on_submit():
        # Check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": form.username.data.lower()})
        # If the user exists flash message & redirect
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        # If the user doesn't exist - append to the database
        register = {
            "username": form.username.data.lower(),
            "password": generate_password_hash(form.password.data)
            }
        mongo.db.users.insert_one(register)
        
        # Put new user in 'session' cookie
        session["user"] = form.username.data.lower()
        flash("Registration Successful!")
        # Take the user to the account page
        return render_template("account.html", username=session["user"])

    # When the Get methord is called load the page with the form on it
    return render_template("register.html", form=form)


@app.route("/login", methods=[ 'GET', 'POST'])
def login():
    # Set up the form
    form = LogInForm()

    # When the Post methord is called and the form is valid.
    if request.method == "POST":
        # Check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": form.username.data.lower()})
        # If the user does exist
        if existing_user:
            # Check hashed passwords match
            if check_password_hash(
                existing_user["password"], form.password.data):
                    session["user"] = form.username.data.lower()
                    flash("Welcome, {}".format(
                        form.username.data.capitalize()))
                    # If they do match redirect the user to the account page
                    return redirect(url_for(
                        "account", username=session["user"]))
            else:
                # Invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            # Invalid username match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

    return render_template("login.html", form=form)


@app.route("/account/<username>")
def account(username):
    # Grab the session user's username from the db
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]

    # ---------- Set up for categories ----------
    # Gets the user categories in alphabetical order
    categories = list(mongo.db.categories.find({
        "created_by": session["user"]
        }).sort("category_name", 1))

    # ---------- Tasks ----------
    # Gets the important tasks and orders them by date 
    importantTasks = list(mongo.db.tasks.find({
        "created_by": session["user"], 
        "is_priority": True, 
        "is_done": False
        }).sort("due_date", 1))
    # Gets the other tasks and orders them by date
    otherTasks = list(mongo.db.tasks.find({
        "created_by": session["user"], 
        "is_priority": False, 
        "is_done": False
        }).sort("due_date", 1))

    # ---------- Task and Progress Bar contents ----------
    # Gets the done tasks and orders them by date/time done
    doneTasks = list(mongo.db.tasks.find({
        "created_by": session["user"], 
        "is_done": True
        }).sort("date_done", -1))

    # ---------- Progress Bar contents ----------
    # Gets the number of important tasks that have been done
    importantDoneTasks = len(list(mongo.db.tasks.find({
        "created_by": session["user"], 
        "is_done": True, 
        "is_priority": True
        })))
    # Number of Important tasks (done + not Done)
    numImportantTasks = importantDoneTasks + len(importantTasks)
    # Number of tasks done that are not important
    lengthOtherUserTasksDone = len(list(mongo.db.tasks.find({
        "created_by": session["user"], 
        "is_priority": False, 
        "is_done": True
        })))
    # Number of Tasks that make up the task bar 
    under = lengthOtherUserTasksDone + numImportantTasks
    
    # ---------- Progress Bar ----------
    # Fill of the Task Bar
    if under == 0:
        progress = 0
    else:
        progress = (100/(under))*(len(doneTasks))
    # Puts the progress in a dictionary
    progressBar = {
        "progress": progress
    }

    # If there is a user in session render account page
    if session["user"]:
        return render_template("account.html", username=username, 
            categories=categories, importantTasks=importantTasks, 
            otherTasks=otherTasks, doneTasks=doneTasks, 
            progressBar=progressBar)

    # If no session user redirect to login page
    return redirect(url_for("login"))


@app.route("/edit_categories/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    # Set up the form
    form = EditCategoryForm()
    # Get the specific category that needs editing
    category = mongo.db.categories.find_one_or_404({
        "_id": ObjectId(category_id)})

    # ---------- Task and Progress Bar contents ----------
    # gets the important tasks and orders them by date
    importantUserTasks = list(mongo.db.tasks.find({
        "created_by": session["user"], 
        "is_priority": True, 
        "is_done": False
        }).sort("due_date", 1))
    # gets the done tasks and orders them by date/time done
    doneTasks = list(mongo.db.tasks.find({
        "created_by": session["user"], 
        "is_done": True
        }).sort("date_done", -1))

    # ---------- Progress Bar contents ----------
    # gets the number of important tasks that have been done
    importantDoneTasks = len(list(mongo.db.tasks.find({
        "created_by": session["user"], 
        "is_done": True, 
        "is_priority": True
        })))
    # Number of Important tasks (done + not Done)
    numImportantTasks = importantDoneTasks + len(importantUserTasks)
    # Number of tasks done that are not important
    lengthOtherUserTasksDone = len(list(mongo.db.tasks.find({
        "created_by": session["user"], 
        "is_priority": False, 
        "is_done": True
        })))
    # Number of Tasks that make up the task bar 
    under = lengthOtherUserTasksDone + numImportantTasks
    
    # ---------- Progress Bar ---------- 
    # Fill of the Task Bar
    if under == 0:
        progress = 0
    else:
        progress = (100/(under))*(len(doneTasks))
    # Puts the progress in a dictionary
    progressBar = {
        "progress": progress
    }

    # Get username from the session user
    username = session['user']

    # Post contents of add category form to mongodb
    if request.method == "POST":
        # Put the edited category in a dictionary
        submit = {
            "category_name": form.task_category.data,
            "created_by": session["user"]
        }
        # Update the selected category
        mongo.db.categories.update({"_id": ObjectId(category_id)},submit)
        flash("Task Successfully Updated")
        # Return to the account
        return redirect(url_for("account", username=username))
    # Puts the information from the category to edit in the form
    elif request.method == 'GET':
        form.task_category.data = category['category_name']
    # If the category cant be fount return an error
    else:
        flash('oops something went wrong!')
        return redirect(request.referrer)

    return render_template("edit_category.html", category=category, 
        form=form, progressBar=progressBar)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    # Get the specific category that is to be deleted
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(request.referrer)


@app.route("/logout")
def logout():
    # Remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("home"))


@app.route("/contact")
def contact():
    # ---------- Task and Progress Bar contents ----------
    # Gets the important tasks and orders them by date
    importantUserTasks = list(mongo.db.tasks.find({
        "created_by": session["user"], 
        "is_priority": True, 
        "is_done": False
        }).sort("due_date", 1))
    # Gets the done tasks and orders them by date/time done
    doneTasks = list(mongo.db.tasks.find({
        "created_by": session["user"], 
        "is_done": True
        }).sort("date_done", -1))

    # ---------- Progress Bar contents ----------
    # Gets the number of important tasks that have been done
    importantDoneTasks = len(list(mongo.db.tasks.find({
        "created_by": session["user"], 
        "is_done": True, 
        "is_priority": True
        })))
    # Number of Important tasks (done + not Done)
    numImportantTasks = importantDoneTasks + len(importantUserTasks)
    # Number of tasks done that are not important
    lengthOtherUserTasksDone = len(list(mongo.db.tasks.find({
        "created_by": session["user"], 
        "is_priority": False, 
        "is_done": True
        })))
    # Number of Tasks that make up the task bar 
    under = lengthOtherUserTasksDone + numImportantTasks
    
    # ---------- Progress Bar ----------
    # Fill of the Task Bar
    if under == 0:
        progress = 0
    else:
        progress = (100/(under))*(len(doneTasks))
    # Puts the progress in a dictionary
    progressBar = {
        "progress": progress
    }

    return render_template("contact.html", progressBar=progressBar)


@app.route("/add_task", methods=[ 'GET', 'POST'])
def add_task():
    # Set up the form
    form = AddTaskForm()

    # ---------- Set up for drop down for add task form ----------
    # Gets the standard categories
    categories_admin = list(mongo.db.categories.find({"created_by": "admin"}))
    # Gets the user categories
    categories_user = list(mongo.db.categories.find({
        "created_by": session["user"]}))
    # Combines the user and standard categories
    categories = (*categories_admin, *categories_user)
    # Extracts category names
    category_names = [(category['category_name']) for category in categories]
    # Sorts the names in alphabetical order
    category_names.sort()
    # Drop down for add task form
    form.task_category.choices = category_names

    # ---------- Task and Progress Bar contents ----------
    # Gets the important tasks and orders them by date
    importantUserTasks = list(mongo.db.tasks.find({
        "created_by": session["user"], 
        "is_priority": True, 
        "is_done": False
        }).sort("due_date", 1))
    # Gets the done tasks and orders them by date/time done
    doneTasks = list(mongo.db.tasks.find({
        "created_by": session["user"], 
        "is_done": True}).sort("date_done", -1))

    # ---------- Progress Bar contents ----------
    # Gets the number of important tasks that have been done
    importantDoneTasks = len(list(mongo.db.tasks.find({
        "created_by": session["user"], 
        "is_done": True, 
        "is_priority": True
        })))
    # Number of Important tasks (done + not Done)
    numImportantTasks = importantDoneTasks + len(importantUserTasks)
    # Number of tasks done that are not important
    lengthOtherUserTasksDone = len(list(mongo.db.tasks.find({
        "created_by": session["user"], 
        "is_priority": False, 
        "is_done": True
        })))
    # Number of Tasks that make up the task bar 
    under = lengthOtherUserTasksDone + numImportantTasks
    
    # ---------- Progress Bar ---------- 
    # Fill of the Task Bar
    if under == 0:
        progress = 0
    else:
        progress = (100/(under))*(len(doneTasks))
    # Puts the progress in a dictionary
    progressBar = {
        "progress": progress
    }

    # Post contents of add task form to mongodb
    if request.method == "POST":
        # If the add a category field is not blank
        if form.add_category.data != "":
            # Find if the category is already on the database
            existing_cat = mongo.db.categories.find_one(
            {"category_name": form.add_category.data.capitalize()})
            if existing_cat:
                # If the category exists then populate cat_name
                cat_name = form.add_category.data.capitalize()
            else:
                # If the category doesn't exist then append it to the db
                category = {
                    "category_name" : form.add_category.data.capitalize(),
                    "created_by": session["user"]
                }
                mongo.db.categories.insert_one(category)
                # Then populate cat_name with the new name
                cat_name = form.add_category.data.capitalize()
                flash("New Category Added")
        # If the add a category field is blank
        # populate cat_name with the task selected from the drop down
        else:
            cat_name = form.task_category.data.capitalize()

        # Get the data from the add_task_form and populate a dictionary
        task = {
            "task_name": form.task_name.data,
            "task_description": form.task_description.data,
            "due_date": str(form.due_date.data),
            "is_priority": form.is_priority.data,
            "is_done": form.is_done.data,
            "task_size": form.task_size.data,
            "category_name": cat_name,
            # Ties the user to the task so it can be viewed later
            "created_by": session["user"]
        }
        # Add the task to the database
        mongo.db.tasks.insert_one(task)
        flash("Task Successfully Added")
        # redirect to the home page
        return redirect(url_for("home"))

    return render_template("add_task.html", form=form, progressBar=progressBar)


@app.route("/edit_task/<task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    # Find the task to edit
    task = mongo.db.tasks.find_one_or_404({"_id": ObjectId(task_id)})
    # Edit task form set up
    form = EditTaskForm()

    # ---------- Set up for drop down for add task form ----------
    # Gets the standard categories
    categories_admin = list(mongo.db.categories.find({"created_by": "admin"}))
    # Gets the user categories
    categories_user = list(mongo.db.categories.find({
        "created_by": session["user"]}))
    # Combines the user and standard categories
    categories = (*categories_admin, *categories_user)
    # Extracts category names
    category_names = [(category['category_name']) for category in categories]
    # Sorts the names in alphabetical order
    category_names.sort()
    # Drop down for add task form
    form.task_category.choices = category_names
    
    # ---------- Task and Progress Bar contents ----------
    # Gets the important tasks and orders them by date
    importantUserTasks = list(mongo.db.tasks.find({
        "created_by": session["user"], 
        "is_priority": True, 
        "is_done": False
        }).sort("due_date", 1))
    # Gets the done tasks and orders them by date/time done
    doneTasks = list(mongo.db.tasks.find({
        "created_by": session["user"], 
        "is_done": True}).sort("date_done", -1))

    # ---------- Progress Bar contents ----------
    # Gets the number of important tasks that have been done
    importantDoneTasks = len(list(mongo.db.tasks.find({
        "created_by": session["user"], 
        "is_done": True, 
        "is_priority": True
        })))
    # Number of Important tasks (done + not Done)
    numImportantTasks = importantDoneTasks + len(importantUserTasks)
    # Number of tasks done that are not important
    lengthOtherUserTasksDone = len(list(mongo.db.tasks.find({
        "created_by": session["user"], 
        "is_priority": False, 
        "is_done": True
        })))
    # Number of Tasks that make up the task bar 
    under = lengthOtherUserTasksDone + numImportantTasks
    
    # ---------- Progress Bar ---------- 
    # Fill of the Task Bar
    if under == 0:
        progress = 0
    else:
        progress = (100/(under))*(len(doneTasks))
    # Puts the progress in a dictionary
    progressBar = {
        "progress": progress
    }

    # If the methord is Post, Post contents of edit task form to mongodb
    if request.method == "POST":
        # If the add a category field is not blank
        if form.add_category.data != "":
            # Find if the category is already on the database
            existing_cat = mongo.db.categories.find_one(
            {"category_name": form.add_category.data.capitalize()})
            if existing_cat:
                # If the category exists then populate cat_name
                cat_name = form.add_category.data.capitalize()
            else:
                # If the category doesn't exist then append it to the db
                category = {
                    "category_name" : form.add_category.data.capitalize(),
                    "created_by": session["user"]
                }
                mongo.db.categories.insert_one(category)
                # Then populate cat_name with the new name
                cat_name = form.add_category.data.capitalize()
                flash("New Category Added")
        # If the add a category field is blank
        # populate cat_name with the task selected from the drop down
        else:
            cat_name = form.task_category.data.capitalize()

        # Get the data from the add_task_form and populate a dictionary
        submit = {
            "task_name": form.task_name.data,
            "task_description": form.task_description.data,
            "due_date": str(form.due_date.data),
            "is_priority": form.is_priority.data,
            "is_done": form.is_done.data,
            "task_size": form.task_size.data,
            "category_name": cat_name,
            # Ties the user to the task so it can be viewed later
            "created_by": session["user"]
        }
        # Update the task on the database
        mongo.db.tasks.update({"_id": ObjectId(task_id)},submit)
        flash("Task Successfully Updated")
        return redirect(url_for("home"))
    # If the methord is Get
    # Puts the information from the task to edit in the form
    elif request.method == 'GET':
        # If the task has a due date
        if task['due_date'] != 'None':
            # Give the date the right format
            due_date = datetime.strptime(task['due_date'], '%Y-%m-%d')
        # Otherwise give the due date a blank string
        else:
            due_date = ''
        # Populate the rest of the form
        form.task_name.data = task['task_name']
        form.task_description.data = task['task_description']
        form.due_date.data = due_date
        form.is_priority.data = task['is_priority']
        form.is_done.data = task['is_done']
        form.task_size.data = task['task_size']
        form.task_category.data = task['category_name']
    # Error handeling - sent back to home.
    else:
        flash('oops something went wrong!')
        return redirect(url_for("home"))

    return render_template("edit_task.html", task=task, form=form, 
        categories=categories, progressBar=progressBar)


@app.route("/delete_task/<task_id>")
def delete_task(task_id):
    # Get the task that is to be deleted and remove it form the database
    mongo.db.tasks.remove({"_id": ObjectId(task_id)})
    flash("Task Successfully Deleted")
    return redirect(url_for("home"))


@app.route("/done_task/<task_id>", methods=["GET", "POST"])
def done_task(task_id):
    # Find the task to edit
    task = mongo.db.tasks.find_one_or_404({"_id": ObjectId(task_id)})
    # Populate the dictionary with the task 
    done = {
        # keeps task populated
        "task_name": task["task_name"],
        "task_description": task["task_description"],
        "due_date": task["due_date"],
        "is_priority": task["is_priority"],
        "task_size": task["task_size"],
        "category_name": task["category_name"],
        "created_by": task["created_by"],
        # toggles of is_done status
        "is_done": not task["is_done"],
        # adds done date
        "date_done": datetime.now()
    }
    # Update the task on the database
    mongo.db.tasks.update({"_id": ObjectId(task_id)},done)
    flash("Task Successfully Done")
    # Refreshed the page
    return redirect(request.referrer)

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
# REMEMBER to change debug to False before submition!!!!!!!!!!!!!!!!!!!!