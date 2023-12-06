from flask import Blueprint, request, render_template, redirect, flash
from app.choreFileReader import readFile

filePath = "/Users/gmp/Documents/GitHub/chore-tracker/Chore Tracker.xlsx" 

tasks_routes = Blueprint("tasks_routes", __name__)

@tasks_routes.route("/tasks/table")
def tasks_table():
    print("tasks table")

    try:
        chore_df = readFile(filePath)
        latest_chore = chore_df.iloc[0] 
        latest_due_date = latest_chore["Due Date"]
        latest_status = "Done" if latest_chore["Status"] else "Pending"
        
        flash("Fetched Latest Chore Data", "success")
        return render_template("table.html", 
                latest_due_date=latest_due_date,
                latest_status=latest_status,
                chore_df = chore_df
        )
    except Exception as err:
        print('OOPS', err)

        flash("Chore data error, please try again!", "danger")
        return redirect("/")

@tasks_routes.route("/tasks/form")
def tasks_form():
    print("tasks form")
    return render_template("tasks.html")

#chore page here