@tasks_routes.route("/tasks/table")
def tasks_table():
    file_path = session.get('file_path')
    if file_path and os.path.exists(file_path):
        try:
            chore_df = readFile(file_path)
            table_html = chore_df.to_html(classes='table table-bordered table-hover', index=False)
            return render_template("table.html", table_html=table_html)
        except Exception as err:
            print('Error reading Excel file:', err)
            flash("Chore data error, please try again!", "danger")
            # Optionally remove the file path from the session if it's invalid
            # session.pop('file_path', None)
    else:
        flash("No Excel file selected. Please upload a file.", "info")

    return render_template("table.html")

@tasks_routes.route("/tasks/form")
def tasks_form():
    file_path = session.get('file_path')
    if file_path and os.path.exists(file_path):
        try:
            chore_df = readFile(file_path)
            tasks_data = chore_df.to_dict('records')
            return render_template("tasks.html", tasks=tasks_data)
        except Exception as err:
            print('Error reading Excel file:', err)
            flash("Error reading file data, please try again!", "danger")
            return redirect("/tasks/table")
    else:
        flash("No Excel file selected. Please upload a file first", "danger")
        return redirect("/tasks/table")
