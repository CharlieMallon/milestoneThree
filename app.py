import os
from flask import (Flask, render_template,
    redirect, url_for, flash, request, session)
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
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
@app.route("/home", methods=[ 'GET', 'POST'])
def home():
    tasks = list(mongo.db.tasks.find())
    add_form = AddTaskForm()
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    category_names = [(category['category_name']) for category in categories]

    add_form.task_category.choices = category_names

    if request.method == "POST":
        task = {
            "task_name": add_form.task_name.data,
            "task_description": add_form.task_description.data,
            "due_date": str(add_form.due_date.data),
            "is_priority": add_form.is_priority.data,
            "is_done": add_form.is_done.data,
            "task_size": add_form.task_size.data,
            "category_name": add_form.task_category.data,
            "created_by": session["user"]
        }
        mongo.db.tasks.insert_one(task)
        flash("Task Successfully Added")
        return redirect(url_for("home"))

    return render_template("home.html", tasks=tasks, form=add_form)


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


@app.route("/account/<username>", methods=[ 'GET', 'POST'])
def account(username):
    # grab the session user's username from the db
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
    
    if session["user"]:
        return render_template("account.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
# REMEMBER to change debug to False before submition!!!!!!!!!!!!!!!!!!!!