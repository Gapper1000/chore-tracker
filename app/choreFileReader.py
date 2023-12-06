import pandas as pd
import os
from openpyxl import load_workbook

filePath = "/Users/gmp/Documents/GitHub/chore-tracker/Chore Tracker.xlsx"
selected_columns = ['Assignee', 'Task', 'Due Date', 'Status']


def readFile(filePath):
        chore_df = pd.read_excel(filePath, usecols=selected_columns)
        # chore_df['Assignee'] = chore_df['Assignee'].astype(object)
        # chore_df['Task'] = chore_df['Task'].astype(str)
        # chore_df['Due Date'] = pd.to_datetime(chore_df['Due Date'], errors='coerce')
        # for index, row in chore_df.iterrows():
        #     if pd.isnull(row['Status']):
        #         chore_df.at[index, 'Status'] = 0
        # chore_df['Status'] = chore_df['Status'].astype(bool)
        return chore_df

def editStatus(chore_df, task_name=str, new_status=bool):
        index = columnIndex(chore_df, 'Task', task_name)
        if index != None:
            chore_df.loc[index, 'Status'] = new_status
        return chore_df

def columnIndex(chore_df, column= str, cell= str):
        try:
            index = chore_df.index[chore_df[column] == cell].tolist()[0]
            return index
        except IndexError:
            print(f"{column} {cell} not found please try again")
            return None
        
def saveToFile(chore_df, filePath):
        """
        Save the updated DataFrame to the Excel file.

        Parameters:
        - chore_df (pd.DataFrame): The updated Chore Tracker DataFrame.
        - filePath (str): The path to the Excel file.
        - sheet_name (str): The name of the sheet in the Excel file. Default is 'ChoreTracker'.
        """
        chore_df.to_excel(filePath, index=False)
        return
    
def duplicateSheet(filePath): #doesnt work here but works in test.py
        """
        Duplicate a sheet in the same Excel file.

        Parameters:
        - filePath (str): The path to the Excel file.
        """
        try:
            workbook = load_workbook(filePath)
            source_sheet_name = workbook.sheetnames[0]
            source_sheet = workbook[source_sheet_name]
            duplicated_sheet_name = f"Copy of {source_sheet_name}"
            duplicated_sheet = workbook.copy_worksheet(source_sheet)
            duplicated_sheet.title = duplicated_sheet_name
            workbook.save(filePath)
            workbook.close()
            return

        except Exception as e:
            print(f"Error duplicating sheet: {e}")
            return

# __name__ == "__main__":


    

    

    

# duplicateSheet(filePath)

# saveToFile(chore_df, filePath)



# chore_df = readFile(chore_df)
# print (chore_df)

# saveToFile(chore_df, filePath)

# chore_df = readFile(chore_df)
# print (chore_df)


# editStatus(chore_df, "Snapper", True)
# saveToFile(chore_df, filePath)

# chore_df = readFile(chore_df)
# print (chore_df)
