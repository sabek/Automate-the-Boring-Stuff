#! python3
# complexPasswordChecker.py - Check password for 8 characters, Upper case, lower case and 1 digit
import re

stripwhitespacestart = re.compile(r'^\s+')
stripwhitespaceend = re.compile(r'\s+$')


def regexstrip(string, stripstring=''):
    if not stripstring:
        string = stripwhitespacestart.sub('', string)
        string = stripwhitespaceend.sub('', string)
        return string
    else:
        striping = re.compile(stripstring)
        string = striping.sub('', string)
        return string


inputstring = input("Type in a string to strip: ")
optionalstrip = input("Type in an optional string to strip: ")

print(regexstrip(inputstring, optionalstrip))