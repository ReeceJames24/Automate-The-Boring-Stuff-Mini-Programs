Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> # multiple assignment
>>> 
>>> cat = ['fat', 'orange', 'loud']
>>> size = cat[0]
>>> color = cat[1]
>>> disposition = cat[3]   #DOING THIS IS TOO HASSLE. Try the one below to do it quicker
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    disposition = cat[3]   #DOING THIS IS TOO HASSLE. Try the one below to do it quicker
IndexError: list index out of range
>>> 
>>> disposition = cat[3]   #DOING THIS IS TOO HASSLE. Try the one below to do it quicker
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    disposition = cat[3]   #DOING THIS IS TOO HASSLE. Try the one below to do it quicker
IndexError: list index out of range
>>> size, color, disposition = cat
>>> size
'fat'
>>> color
'orange'
>>> disposition
'loud'
>>> 
>>> 
>>> # ASSIGNMENT SWAPPING
>>> 
>>> a = cat
>>> b = dog
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    b = dog
NameError: name 'dog' is not defined
>>> 