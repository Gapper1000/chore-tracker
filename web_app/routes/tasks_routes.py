from flask import Blueprint, request, render_template, redirect, flash, session, send_from_directory
from app.choreFileReader import readFile, update_workbook
import os
from werkzeug.utils import secure_filename

tasks_routes = Blueprint("tasks_routes", __name__)

@tasks_routes.route("/tasks/table", methods=["GET", "POST"])
def tasks_table():
    if request.method == "POST":
        file = request.files.get("file")

        if file and file.filename != '':
            # Process the uploaded file
            filename = secure_filename(file.filename)
            file_path = os.path.join("uploads", filename)
            full_file_path = os.path.abspath(file_path)  # Get the absolute file path
            file.save(full_file_path)
            session['file_path'] = full_file_path  # Store the absolute file path in the session
            session['file_name'] = filename
        else:
            # If no file was uploaded in this POST request
            flash("No file uploaded. Please upload a file.", "danger")

    # The rest of your code...


    if 'file_path' in session:
        # If there is a file in the session, try to read and display it
        try:
            file_path = session['file_path']
            chore_df = readFile(file_path)
            table_html = chore_df.to_html(classes='table table-bordered table-hover', index=False)
            flash("Fetched Latest Chore Data", "success")
            return render_template("table.html", table_html=table_html)
        except Exception as err:
            print('OOPS', err)
            flash("Chore data error, please try again!", "danger")
            session.pop('file_path', None)  # Remove invalid file path from session
            return render_template("table.html")  # Still render the table page, but without data

    # If there is no file in the session, just show the page with upload option
    return render_template("table.html")

@tasks_routes.route("/tasks/form")
def tasks_form():
    file_name = session.get('file_name')
    file_path = session.get('file_path')

    if file_path:
        try:
            chore_df = readFile(file_path)
            tasks_data = chore_df.to_dict('records')
            return render_template("tasks.html", tasks=tasks_data)
        except Exception as err:
            print('OOPS', err)
            flash("Error reading file data, please try again!", "danger")
            return redirect("/tasks/table")
    else:
        flash("No file selected, please upload a file first", "danger")
        return redirect("/tasks/table")

@tasks_routes.route("/tasks/update", methods=["POST"])
def update_tasks():
    checked_tasks = request.form.getlist('tasks')

    try:
        update_workbook(session['file_path'], checked_tasks)
        flash("Tasks updated successfully", "success")
    except Exception as e:
        flash(f"An error occurred while updating tasks: {e}", "danger")

    return redirect('/tasks/table')

@tasks_routes.route("/download-file")
def download_file():
    print("download file")
    file_path = session.get('file_path')
    print(file_path)
    if file_path:
        # Extract directory and filename from the file_path
        directory = os.path.dirname(file_path)
        print(directory)
        filename = os.path.basename(file_path)
        print(filename)
        return send_from_directory(directory, filename, as_attachment=True)
    else:
        flash("No file available for download.", "danger")
        return redirect('/tasks/table')
