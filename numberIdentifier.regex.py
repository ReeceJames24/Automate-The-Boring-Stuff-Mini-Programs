import re

phoneNumRegex = re.compile(r'\d\d\d\d-\d\d\d-\d\d\d\d')
# re.compile allows you to store the string as a regex object
# r allows you to bypass the \ since you ned to use \ a lot in regex

print('Input Statement')
message = str(input())
mo = phoneNumRegex.search(message)
print(mo.group())





