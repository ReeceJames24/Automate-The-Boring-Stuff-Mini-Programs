Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #REGEX GROUPING NOTES
>>> 
>>> 

>>> import re
>>> namesRegex = re.compile(r'Agent (\w)\w*')
>>> message = 'Agent Eggs gave the documents to Agent Bobs'
>>> namesRegex.findall(message)
['E', 'B']
>>> mo = namesRegex.search(message)
>>> mo.group()
'Agent Eggs'
>>> # NOTE that for search method, you get to match the whole pattern even when your regex object has grouping
>>> 
>>> # BUTTT when you do findall method, it will find the entire pattern BUT return only the grouped regex (inside the parentheses) once it finds a match)
>>> 
>>> #thats why it only returned 'E' and 'B' awhile ago