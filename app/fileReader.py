import pandas as pd
import openpyxl

filePath = "/Users/gmp/Documents/GitHub/chore-tracker/Chore Tracker.xlsx"

df = pd.read_excel(filePath)
print(df)
