from flask import Blueprint, request, render_template, redirect, flash
from app.choreFileReader import readFile
import os
from werkzeug.utils import secure_filename

filePath = "/Users/gmp/Documents/GitHub/chore-tracker/Chore Tracker.xlsx"

tasks_routes = Blueprint("tasks_routes", __name__)

@tasks_routes.route("/tasks/table", methods=["GET", "POST"])
def tasks_table():
    print("tasks/table")

    if request.method == "POST":
        # Check if the POST request has the file part
        if "file" not in request.files:
            flash("No file part", "danger")
            return redirect(request.url)

        file = request.files["file"]

        # If the user does not select a file, the browser will submit an empty file
        if file.filename == "":
            flash("No selected file", "danger")
            return redirect(request.url)

        if file:
            # Save the file to a secure location
            filename = secure_filename(file.filename)
            file.save(os.path.join("uploads", filename))

            try:
                chore_df = readFile(os.path.join("uploads", filename))
                table_html = chore_df.to_html(classes='table table-bordered table-hover', index=False)
                flash("Fetched Latest Chore Data", "success")
                return render_template("table.html", table_html=table_html)
            except Exception as err:
                print('OOPS', err)
                flash("Chore data error, please try again!", "danger")
                return redirect("/")
                
    else:
        try:
            chore_df = readFile(filePath)
            print(chore_df)
            table_html = chore_df.to_html(classes='table table-bordered table-hover', index=False)

            flash("Fetched Latest Chore Data", "success")
            return render_template("table.html", table_html=table_html)
        except Exception as err:
            print('OOPS', err)
            flash("Chore data error, please try again!", "danger")
            return redirect("/")

@tasks_routes.route("/tasks/form")
def tasks_form():
    print("tasks form")
    return render_template("tasks.html")
