import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Set up credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Specify the path to your JSON key file (replace with the actual path)
json_key_path = "/Users/gmp/Documents/GitHub/chore-tracker/config/freestyle-project-407217-3968e1b66986.json"
creds = ServiceAccountCredentials.from_json_keyfile_name(json_key_path, scope)

# Authenticate with Google Sheets API
client = gspread.authorize(creds)

# Open the Google Sheet by title
sheet = client.open_by_key("1rta3xYgJb-2iWAAw0lXJ1LiB0Z0OOLTyRZQ7HNSnB14").sheet1

# Get all values from the sheet
all_values = sheet.get_all_values()

# Print the values
for row in all_values:
    print(row)
