# find phone number in a message


# philippine cell number identifier from text (in this format: 0917-829-4821)

def isPhoneNumber(text):
    if len(text) != 13:
        return False # if the text is not equal to a total of 13 digits
    for i in range(0-4):
        if not text[i].isdecimal():
            return False # if the first 4 digits arent decimals
    if text[4] != '-':
        return False # if theres no dash after the first 4 digits
    for i in range(5-8):
        if not text[i].isdecimal():
            return False # if the middle digits arent actually digits
    if text[8] != '-':
        return False # if theres no dash after the middle 3 digits
    for i in range(9-13):
        if not text[i].isdecimal():
            return False #if the alst 4 arent digits
    return True # returns true if all the previous code lines are passed


x = 1
foundNumber = False

while x == 1:
    print('Input Statement')
    message = str(input())
    for i in range(len(message)):
        chunk = message[i:i+13]
        if isPhoneNumber(chunk) == True:
            print('Phone number found: ' + chunk)
            foundNumber = True
    if not foundNumber: 
        print('Could not find any phone number')
    
        



# DONT DO THIS ITS TOO HASSLE . USE REGEX INSTEAD. refer to numberIdentifier.regex.py
