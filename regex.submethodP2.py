Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Regex submethod part 2
>>> 
>>> 
>>> import re
>>> namesRegex = re.compile (r'Agent(\w)\w+')
>>> # now we have set the grouping of the first letter so we can show it in findall
>>> # note that (\w) is automatically assigned as group 1
>>> 
>>> Log = 'Agent Axe gave the documents to Agent Bilbo'
>>> #now we use referencing in the sub method in order to pulll the first group and show it in the match
>>> 
>>> namesRegex.sub(r'Agent \1*****', Log)
'Agent Axe gave the documents to Agent Bilbo'
>>> #OOPS
>>> 
>>> #wrong object
>>> 
>>> #let us redo that
>>> 
>>> namesRegex = re.compile (r'Agent (\w)\w*')
>>> Log = 'Agent Axe gave the documents to Agent Bilbo'
>>> namesRegex.sub(r'Agent \1****', Log)
'Agent A**** gave the documents to Agent B****'
>>> #there we go
>>> #we need to put r to indicate raw string
>>> # since we need to use \1 to indicate "pull group 1 of the found matched pattern"
>>> # how sub works i basically, you first create your regex pattern with re.compile
>>> #then you pass the string you want to check as second argument in the sub method and you indicate the "replace with" portion with the 1st argument
>>> 
>>> #BASICALLY FIND AND REPLACE IN EXCEL
>>> 
>>> 