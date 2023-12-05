import getpass
import os
from dotenv import load_dotenv

load_dotenv()

usernameOS = os.getenv("userLogin")
passwordOS = os.getenv("passwordLogin")

def login():
    loginSuccess = False
    if username == usernameOS and password == passwordOS:
        loginSuccess = True
    else:
        loginSuccess = False
    return loginSuccess