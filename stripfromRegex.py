#!python 3
import re

stripChar = input('Enter character to strip: ')
context = input('Enter string to strip: ')
stripContext = None


def strip(char,string):
    if char == "":                # not "stripChar"
        regsp = re.compile(r'^\s+|\s+$')
        stripContext = regsp.sub("", context)
        return stripContext
    else:                       # some changes are here in this else statement
        stripContext = re.sub(r'(char)+', "", context)
        return stripContext


print(strip(stripChar,context))
