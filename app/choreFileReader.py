import pandas as pd
import openpyxl

filePath = "/Users/gmp/Documents/GitHub/chore-tracker/Chore Tracker.xlsx"
selected_columns = ['Assignee', 'Task', 'Due Date', 'Status']
chore_df = pd.read_excel(filePath, usecols=selected_columns)

if __name__ == "__main__":


    def readFile(chore_df):
        chore_df['Assignee'] = chore_df['Assignee'].astype(object)
        chore_df['Task'] = chore_df['Task'].astype(str)
        chore_df['Due Date'] = pd.to_datetime(chore_df['Due Date'], errors='coerce')
        for index, row in chore_df.iterrows():
            if pd.isnull(row['Status']):
                chore_df.at[index, 'Status'] = False
        chore_df['Status'] = chore_df['Status'].astype(bool)
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

chore_df = readFile(chore_df)
print (chore_df)

# editStatus(chore_df, "Snapper", True)
# print (chore_df)





