#!/usr/local/bin/python3

#PHONE NUMBER AND EMAIL FINDER

import re, pyperclip

#TO DO: Create Regex for Phone Numbers
phoneREGEX = re.compile(r'''

# possible number formats: 515-555-9870, 555-9870, (515) 513-7770, 555-5786 ext 12345, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))           # area code (ill make this non optional)
(\s|-)            # first seaprator
\d\d\d           # mid 3 digits
(\s|-)            # second separator
\d\d\d\d            # last 4 digits
(\s(ext(\.)?|x)(\s)?(\d{2,5}))?   #extension (optional)
)                  #putting open parenthesis at the start and end sets the whole regex as GROUP 1. this is so you you can use the findall method without it returning lists of tuples of strings per group (which you have a ton of in the pattern)
''', re.VERBOSE)


#TO DO: Create Regex for Email Addresses
emailREGEX = re.compile(r'''

#possible email pattern: something.+_@something.com

[a-zA-Z0-9+_.]+      #3rd level domain
@                  # @ sign
[a-zA-Z0-9+_.]+      # 2nd level domain
\.[a-zA-Z0-9+_.]{1,3}  # top level domain (.com part)
''',re.VERBOSE)
#TO DO: Get the text off of the clipboard
text = pyperclip.paste()


#TO DO: Extract the email/phone num from this text
extractedNUM = phoneREGEX.findall(text) 
extractedEMAIL = emailREGEX.findall(text)


CompleteNums = [] #since the findall will give the complete number as the first string in the tuple, we want to get only that string in each tuple (since the other strings in each tuple will have all the different mini groups)


for tupleZ in extractedNUM:
    CompleteNums.append(tupleZ[0])
    
#this will add only the complete num per found tuple in findall to the CompleteNums list

#TO DO: Copy extracted data to clipboard
completeData = '\n'.join(CompleteNums) + '\n' + '\n'.join(extractedEMAIL)
pyperclip.copy(completeData)


print('Sample')
print(completeData[:195])
print('Extracted data has now been copied to your clipboard')













