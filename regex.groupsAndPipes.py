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
>>> 
>>> # if your pattern includes parentheses, you have to backslash it in the regex object
>>> 
>>> #example
>>> 
>>> message = 'My phone number is (0917) 335-6680'
>>> phoneNumRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
>>> mo = phoneNumRegex.search(message)
>>> mo.group()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    mo.group()
AttributeError: 'NoneType' object has no attribute 'group'
>>> #oops wrong regex
>>> phoneNumRegex = re.compile(r'\(\d\d\d\d\) \d\d\d-\d\d\d\d')
>>> mo.group()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    mo.group()
AttributeError: 'NoneType' object has no attribute 'group'
>>> #OOPS
>>> phoneNumRegex = re.compile(r'\(\d\d\d\d\) \d\d\d-\d\d\d\d')
>>> mo = phoneNumRegex.search(message)
>>> mo.group()
'(0917) 335-6680'
>>> # NICE
>>> 
>>> 
>>> #using Pipes
>>> 
>>> message = 'Batmobile is the name of myr at'
>>> batRegex = re.compile(r'Bat(man|mobile|rat|cat|bat|woman|girl)')
>>> mo = batRegex.search(message)
>>> mo.group()
'Batmobile'
>>> # NICE
>>> 
>>> #note that if the search method cant find the regex pattern in the string that you pass it, its going to return none
>>> #so if you try to call mo.group() for no pattern found, you'll get an error
>>> 
>>> #see example
>>> 
>>> message = 'Ratty hat tat'
>>> mo = batRegex.search(message)
>>> mo == None
True
>>> mo.group()
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    mo.group()
AttributeError: 'NoneType' object has no attribute 'group'
>>> # see lel
>>> 
>>> mo.group(1)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    mo.group(1)
AttributeError: 'NoneType' object has no attribute 'group'
>>>  message = 'Batmobile is the name of myr at'
 
SyntaxError: unexpected indent
>>> message = 'Batmobile is the name of myr at'
>>> mo = batRegex.search(message)
>>> mo.group()
'Batmobile'
>>> mo.group(1)
'mobile'
>>> mo.group(2)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    mo.group(2)
IndexError: no such group
>>> #Ok
>>> 