from getpass import getpass, getuser
import os
from dotenv import load_dotenv

load_dotenv()

usernameOS = os.getenv("userLogin")
passwordOS = os.getenv("passwordLogin")

def login(username, password):
    loginSuccess = False
    if username == usernameOS and password == passwordOS:
        loginSuccess = True
    else:
        loginSuccess = False
    return loginSuccess

def checkLogin(session):
    if 'username' not in session:
        return False
    else:
        return True
