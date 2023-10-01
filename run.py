import gspread
from google.oauth2.service_account import Credentials
import json

# Every Google account has as an IAM (Identity and Access Management)
# configuration which specifies what the user has access to.
# The SCOPE lists the APIs that the program should access in order to run.

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

creds = json.load(open('creds.json'))
CREDS = Credentials.from_service_account_info(creds)
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("animal_game")

"""
Terminal based animal quiz game
"""
def rungame():
    print("You now have the following options")

playername = input("Welcome to the amazing animal quiz game please enter your name\n")

if len(playername) <= 20:
    print("Entry is valid!")
    rungame()
else:
    input("Please enter a name shorter than 20 characters\n")   


#print("Welcome " + playername + " please select an option below:\n")

