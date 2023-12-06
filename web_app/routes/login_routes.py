from flask import Blueprint, request, render_template, flash, redirect, session, url_for
from app.login import login

login_routes = Blueprint("login_routes", __name__)

def checkLogin(session):
    return 'username' in session

@login_routes.route("/login/form", methods=["GET", "POST"])
def login_form():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        login_success = login(username, password)

        if login_success:
            session['username'] = username
            flash("Login successful!", "success")
            print("Login:", login_success)
            return redirect("/tasks/table")
        else:
            flash("Login failed. Please check your credentials.", "danger")
            print("Login:", login_success)

    return render_template("login.html")

@login_routes.route("/logout")
def logout():
    # Clear the session
    session.clear()
    # Redirect to the login page or any other page after logout
    return redirect(url_for("/login/form"))
