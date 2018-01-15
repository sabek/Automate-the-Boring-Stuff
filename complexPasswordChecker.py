#! python3
# complexPasswordChecker.py - Check password for 8 characters, Upper case, lower case and 1 digit
import re

checkupperregex = re.compile(r'[A-Z]+')
checklowerregex = re.compile(r'[a-z]+')
checkdigitregex = re.compile(r'[0-9]+')


def checkpasswordstrength(password):
    if len(password) < 8:
        return "Your password is too short."
    elif checkupperregex.search(password) and checklowerregex.search(password) and checkdigitregex.search(password):
        return "Password acceptable."
    else:
        return "Password does not meet criteria."


print(checkpasswordstrength(input("Type in a password to check: ")))
