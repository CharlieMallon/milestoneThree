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
    tasks = list(mongo.db.tasks.find())

    return render_template("home.html", tasks=tasks)


@app.route("/register", methods=[ 'GET', 'POST'])
def register():
    reg_form = RegistrationForm()
    if request.method == "POST" and reg_form.validate_on_submit():
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": reg_form.username.data.lower()})
        #if the user exists flash message & redirect
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        #if the user doesn't exist - append to the database
        register = {
            "username": reg_form.username.data.lower(),
            "password": generate_password_hash(reg_form.password.data)
            }
        mongo.db.users.insert_one(register)
        
        #put new user in 'session' cookie
        session["user"] = reg_form.username.data.lower()
        flash("Registration Successful!")
        return render_template("account.html", username=session["user"])

    return render_template("register.html", form=reg_form)


@app.route("/login", methods=[ 'GET', 'POST'])
def login():
    log_form = LogInForm()
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": log_form.username.data.lower()})

        if existing_user:
            # check hashed passwords match
            if check_password_hash(
                existing_user["password"], log_form.password.data):
                    session["user"] = log_form.username.data.lower()
                    flash("Welcome, {}".format(
                        log_form.username.data.capitalize()))
                    return redirect(url_for(
                        "account", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # invalid username match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

    return render_template("login.html", form=log_form)


@app.route("/account/<username>")
def account(username):
    # grab the session user's username from the db
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
    
    # ----- set up for drop down for add task form
    # gets the user categories
    categories = list(mongo.db.categories.find({"created_by": session["user"]}))
    # extracts category names
    category_names = [(category['category_name']) for category in categories]
    # sorts the names in alphabetical order
    category_names.sort()

    if session["user"]:
        return render_template("account.html", username=username, categories=categories)

    return redirect(url_for("login"))


@app.route("/edit_categories/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    # form
    form = EditCategoryForm()
    # category
    category = mongo.db.categories.find_one_or_404({"_id": ObjectId(category_id)})
    # grab the session user's username from the db
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]

    # Post contents of add category form to mongodb
    if request.method == "POST":

        submit = {
            "category_name": form.task_category.data,
            "created_by": session["user"]
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)},submit)
        flash("Task Successfully Updated")
        return redirect(request.referrer)
    # Puts the information on the task to edit in the form
    elif request.method == 'GET':
        form.task_category.data = category['category_name']
    else:
        flash('oops something went wrong!')
        return redirect(request.referrer)

    return render_template("edit_category.html", category=category, form=form)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(request.referrer)


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/add_task", methods=[ 'GET', 'POST'])
def add_task():
    # Add task form set up
    add_form = AddTaskForm()
    # ----- set up for drop down for add task form
    # gets the standard categories
    categories_admin = list(mongo.db.categories.find({"created_by": "admin"}))
    # gets the user categories
    categories_user = list(mongo.db.categories.find({"created_by": session["user"]}))
    # combines the user and standard categories
    categories = (*categories_admin, *categories_user)
    # extracts category names
    category_names = [(category['category_name']) for category in categories]
    # sorts the names in alphabetical order
    category_names.sort()

    # Drop down for add task form
    add_form.task_category.choices = category_names

    # Post contents of add tsk form to mongodb
    if request.method == "POST":

        if add_form.add_category.data != "":
            existing_cat = mongo.db.categories.find_one(
            {"category_name": add_form.add_category.data.capitalize()})
            if existing_cat:
                cat_name = add_form.add_category.data.capitalize()
            else:
                category = {
                    "category_name" : add_form.add_category.data.capitalize(),
                    "created_by": session["user"]
                }
                mongo.db.categories.insert_one(category)
                cat_name = add_form.add_category.data.capitalize()
                flash("New Category Added")
        else:
            cat_name = add_form.task_category.data.capitalize()

        task = {
            "task_name": add_form.task_name.data,
            "task_description": add_form.task_description.data,
            "due_date": str(add_form.due_date.data),
            "is_priority": add_form.is_priority.data,
            "is_done": add_form.is_done.data,
            "task_size": add_form.task_size.data,
            "category_name": cat_name,
            # Ties the user to the task so it can be viewed later
            "created_by": session["user"]
        }
        mongo.db.tasks.insert_one(task)
        flash("Task Successfully Added")
        # redirect to origin page
        return redirect(url_for("home"))
    return render_template("add_task.html", form=add_form)


@app.route("/edit_task/<task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    # find the task to edit
    task = mongo.db.tasks.find_one_or_404({"_id": ObjectId(task_id)})
    # edit task form set up
    form = EditTaskForm()

    # ----- set up for drop down for add task form
    # gets the standard categories
    categories_admin = list(mongo.db.categories.find({"created_by": "admin"}))
    # gets the user categories
    categories_user = list(mongo.db.categories.find({"created_by": session["user"]}))
    # combines the user and standard categories
    categories = (*categories_admin, *categories_user)
    # extracts category names
    category_names = [(category['category_name']) for category in categories]
    # sorts the names in alphabetical order
    category_names.sort()

    # Drop down for add task form
    form.task_category.choices = category_names

    # Post contents of add task form to mongodb
    if request.method == "POST":

        if form.add_category.data != "":
            existing_cat = mongo.db.categories.find_one(
            {"category_name": form.add_category.data.capitalize()})
            if existing_cat:
                cat_name = form.add_category.data.capitalize()
            else:
                category = {
                    "category_name" : form.add_category.data.capitalize(),
                    "created_by": session["user"]
                }
                mongo.db.categories.insert_one(category)
                cat_name = form.add_category.data.capitalize()
                flash("New Category Added")
        else:
            cat_name = form.task_category.data.capitalize()

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
        mongo.db.tasks.update({"_id": ObjectId(task_id)},submit)
        flash("Task Successfully Updated")
        return redirect(url_for("home"))
    # Puts the information on the task to edit in the form
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
        flash('oops something went wrong!')
        return redirect(url_for("home"))

    return render_template("edit_task.html", task=task, form=form, categories=categories)


@app.route("/delete_task/<task_id>")
def delete_task(task_id):
    mongo.db.tasks.remove({"_id": ObjectId(task_id)})
    flash("Task Successfully Deleted")
    return redirect(url_for("home"))


@app.route("/done_task/<task_id>", methods=["GET", "POST"])
def done_task(task_id):
    # find the task to edit
    task = mongo.db.tasks.find_one_or_404({"_id": ObjectId(task_id)})
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
        "is_done": not task["is_done"]
    }
    mongo.db.tasks.update({"_id": ObjectId(task_id)},done)
    flash("Task Successfully Done")
    return redirect(request.referrer)

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
# REMEMBER to change debug to False before submition!!!!!!!!!!!!!!!!!!!!