Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # HOW TO MATCH CASE INSENSITIVELY
>>> 
>>> 
>>> # the hassle way to do it is to input both lower case and upper case manually
>>> vowelFinder = re.compile(r'[aeiouAEIOU]')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    vowelFinder = re.compile(r'[aeiouAEIOU]')
NameError: name 're' is not defined
>>> #OOPS FORGOT TO IMPORT MODULE
>>> 
>>> import re
>>> vowelFinder = re.compile(r'[aeiouAEIOU]')
>>> message = 'Hi! where do I go to find the nearest Cheken Wiengs'
>>> vowelFinder.findall(message)
['i', 'e', 'e', 'o', 'I', 'o', 'o', 'i', 'e', 'e', 'a', 'e', 'e', 'e', 'i', 'e']
>>> #this works but if you're matching a ot of letters, then you would want to save time by not typing the capital version of each letter
>>> # what oyu can do is to pass the re.I or re.IGNORECASE as a second argument to the compile function
>>> 
>>> vowelFinder = re.compile(r'[aeiou]',re.I)
>>> message = 'Hi! where do I go to find the nearest Cheken Wiengs'
>>> vowelFinder.findall(message)
['i', 'e', 'e', 'o', 'I', 'o', 'o', 'i', 'e', 'e', 'a', 'e', 'e', 'e', 'i', 'e']
>>> #SEE EZer