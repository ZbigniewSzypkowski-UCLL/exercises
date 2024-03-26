import re

users = {}

def validate_password(password):
    if re.match("(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(.{8})", password) != None:
        return True
    else:
        return False

def register():
    username = input("\n\n\nPlease enter an username: ")
    password = input("Please enter an password: ")
    if validate_password(password):
        users[username] = password
        print("\nRegistration successfull!")
    else:
        print("\nRegistration Failed: password not permited!\nAborting operation!\n")


register()