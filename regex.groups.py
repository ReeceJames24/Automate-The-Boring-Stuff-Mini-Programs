Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> # regex groups
>>> 
>>> import re
>>> phoneNumRegex = re.compile(r'\d\d\d\d-\d\d\d-\d\d\d\d')
>>> message = 'My Phone Number is 0916-181-5388'
>>> mo = phoneNumRegex.search(message)
>>> mo.group()
'0916-181-5388'
>>> 
>>> #if you want to get only the first 4 digits, you need to create groups
>>> # you create groups using parentheses
>>> 
>>> phoneNumRegex = re.compile(r'(\d\d\d\d)-(\d\d\d)-(\d\d\d\d)')
>>> mo = phoneNumRegex.search(message)
>>> mo.group()
'0916-181-5388'
>>> mo.group(1)
'0916'
>>> mo.group(2)
'181'
>>> mo.group(3)
'5388'
>>> #NICE