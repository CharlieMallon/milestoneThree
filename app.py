import os
from flask import Flask, render_template, redirect, url_for, flash
from flask_pymongo import PyMongo
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
    if reg_form.validate_on_submit():
        flash("Registration Successful!")
        return redirect(url_for('home'))
    return render_template("register.html", form=reg_form)


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/account")
def account():
    return render_template("account.html")


@app.route("/logout")
def logout():
    return redirect(url_for("home"))


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
# REMEMBER to change debug to False before submition!!!!!!!!!!!!!!!!!!!!