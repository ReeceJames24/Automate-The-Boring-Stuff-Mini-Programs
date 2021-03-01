Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Regex sub() method means to substitute the found pattern (basically the find and replace method)p
>>> 
>>> import re
>>> namesRegex = re.compile(r'Agent \w+')
>>> Log = 'Agent Alice gave the documents to Agent Jimboo'
>>> namesRegex.findall(Log)
['Agent Alice', 'Agent Jimboo']
>>> # we use the sub method if we want to keep the identities of the agents hidden
>>> 
>>> namesRegex.sub('REDACTED', message)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    namesRegex.sub('REDACTED', message)
NameError: name 'message' is not defined
>>> #OOPS
>>> 
>>> namesRegex.sub('REDACTED', Log)
'REDACTED gave the documents to REDACTED'
>>> #now their identities are safe
>>> 
>>> #however we need to adjust it if we want the first letter of their names to be shown at the leeast
>>> 