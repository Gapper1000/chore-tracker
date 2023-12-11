from flask import Blueprint, request, render_template, redirect, flash, session
from app.choreFileReader import readFile
import os
from werkzeug.utils import secure_filename

filePath = "/Users/gmp/Documents/GitHub/chore-tracker/Chore Tracker.xlsx"

tasks_routes = Blueprint("tasks_routes", __name__)

@tasks_routes.route("/tasks/table", methods=["GET", "POST"])
def tasks_table():
    if request.method == "POST":
        file = request.files.get("file")  # Using get method to avoid KeyError if 'file' is not in request.files

        if file and file.filename != '':  # Check if the file exists and has a filename
            filename = secure_filename(file.filename)
            file.save(os.path.join("uploads", filename))

            try:
                chore_df = readFile(os.path.join("uploads", filename))
                session['file_name'] = filename
                table_html = chore_df.to_html(classes='table table-bordered table-hover', index=False)
                flash("Fetched Latest Chore Data", "success")
                return render_template("table.html", table_html=table_html)
            except Exception as err:
                print('OOPS', err)
                flash("Chore data error, please try again!", "danger")
                return redirect("/")
        else:
            # Handle the case where no file is uploaded
            flash("No file uploaded. Please upload a file.", "danger")
            return redirect("/tasks/table")

    else:
        try:
            chore_df = readFile(filePath)
            session['file_name'] = "Chore Tracker.xlsx"
            table_html = chore_df.to_html(classes='table table-bordered table-hover', index=False)
            flash("Fetched Latest Chore Data", "success")
            return render_template("table.html", table_html=table_html)
        except Exception as err:
            print('OOPS', err)
            flash("Chore data error, please try again!", "danger")
            return redirect("/tasks/table")


@tasks_routes.route("/tasks/form")
def tasks_form():

    file_name = session.get('file_name')

    if file_name:
        try:
            chore_df = readFile(os.path.join("uploads", file_name))
            tasks_data = chore_df.to_dict('records')
            return render_template("tasks.html", tasks=tasks_data)
        except Exception as err:
            print('OOPS', err)
            flash("Error reading file data, please try again!", "danger")
            return redirect("/tasks/table")
    else:
        flash("No file selected, please upload a file first", "danger")
        return redirect("/tasks/table")
