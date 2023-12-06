#login routes here

#remove llogin routes from home routes?

#how do I save login data so it does it for the individual person?

from flask import Blueprint, request, render_template, flash, redirect
from app.login import login

login_routes = Blueprint("login_routes", __name__)

@login_routes.route("/login/form", methods=["GET", "POST"])
def login_form():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        login_success = login(username, password)

        if login_success == True:
            flash("Login successful!", "success")
            print("Login:", login_success)
            return redirect("/tasks/table")  
        else:
            flash("Login failed. Please check your credentials.", "danger")
            print("Login:", login_success)

    return render_template("login.html")

    