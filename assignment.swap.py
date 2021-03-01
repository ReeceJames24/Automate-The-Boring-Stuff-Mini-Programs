Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> # assignment swaps
>>> 
>>> a = cat
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a = cat
NameError: name 'cat' is not defined
>>> a = 'cat'
>>> b = 'dog'
>>> a, b = b, a
>>> a
'dog'
>>> b
'cat'
>>> 
>>> 
>>> a, b, c = 'cat', 'fat', 'rat'
>>> a
'cat'
>>> b
>>> c
'rat'
>>> b
'fat'
>>> a, b, c = c, b, a
>>> a
'rat'
>>> b
'fat'
>>> c
'cat'
>>> 