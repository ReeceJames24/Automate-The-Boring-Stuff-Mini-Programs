Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # repetition in regex patterna
>>> 
>>> 
>>> import re
>>> # we can use the ? character to denote "occurs 0 or 1 time/s"
>>> 
>>> numRegex = re.compile(r'Bat(wo)?man')
>>> message = 'I Am going to watch Batman'
>>> mo = numRegex.search(message)
>>> mo.group()
'Batman'
>>> message = 'I Am going to watch Batwoman'
>>> mo.group()
'Batman'
>>> #OOPS
>>> 
>>> message = 'I Am going to watch Batman'
>>> #oops again
>>> 
>>> message = 'I am going to watch Batwoman'
>>> mo = numRegex.search(message)
>>> mo.group()
'Batwoman'
>>> #NICE
>>> #but it wont work if you repeat the wo
>>> 
>>> message = 'I am going to watch Batwowowowoman'
>>> mo = numRegex.search(message)
>>> mo.group()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    mo.group()
AttributeError: 'NoneType' object has no attribute 'group'
>>> mo == None
True
>>> #see :+{
>>> 
>>> #to do this you need to use either the + symbol (1 or more) or the * symbol (0 or more)
>>> 
>>> 
>>> batRegex = re.compile(r'Bat(wo)*man')
>>> mo = batRegex.search(message)
>>> message = 'I am Batwowowowowoman'
>>> mo.group()
'Batwowowowoman'
>>> # NICE
>>> 
>>> #if you need to find a pattern that includes the ? or * or + symbols, you use the backslash to escape it
>>> 
>>> 
>>> symbol = '?*+'
>>> eggs = re.compile(r'?\*\+\')
		  
SyntaxError: EOL while scanning string literal
>>> #ooops
>>> 
>>> eggs = re.compile(r'\?\*\+')
>>> mo  = eggs.search(symbol)
>>> mo.group()
'?*+'
>>> #NICE
>>> # if youre looking for any number of times for these symbols to show, use the characters without escape. See example below
>>> 
>>> 
>>> Regex = re.compile(r'(\?)*(\*)*(\+)*')
>>> mo = Regex.search(message)
>>> message = '???*++++++++++'
>>> mo.group()
''
>>> #OOPS WRONG SORRY
>>> 
>>> Regex = re.compile(r'\?*\**\+*')
>>> message = '?*+++++'
>>> mo = Regex.search(message)
>>> mo.group()
'?*+++++'
>>> # NICE
>>> # more example
>>> 
>>> regex = re.compile(r'(\+\*\?)+')
>>> mo = regex.search(message)
>>> message = 'nice i like to eat +*?+*?'
>>> mo.group()
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    mo.group()
AttributeError: 'NoneType' object has no attribute 'group'
>>> #ooops
>>>  regex = re.compile(r'(\+\*\?)+')
 
SyntaxError: unexpected indent
>>> regex = re.compile(r'(\+\*\?)+')
>>> message = 'Ni ce i like to eat +*?+*?+*?'
>>> mo = regex.search(message)
>>> mo.group()
'+*?+*?+*?'
>>> #NICEE

>>> 

>>> regex = re.compile(r'(\?)*(\*)*(\+)*')
>>> message = '???*++++++++++'
>>> mo = regex.search(message)
>>> mo.group()
'???*++++++++++'
>>> #NICE
>>> 
>>> 
>>> # if you want to exact a pattern or character a specific number of times, use curly brackets {x} where x = number of repetitions
>>> 
>>> regex = re.compile(r'eggs{3}(rats)*(ranch)+')
>>> message = 'i want to go to eggseggseggsranch'
>>> mo = regex.search(message)
>>> mo.group()
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    mo.group()
AttributeError: 'NoneType' object has no attribute 'group'
>>> mo.group() == None
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    mo.group() == None
AttributeError: 'NoneType' object has no attribute 'group'
>>> # NAKO PO SORRY
>>> 
>>> #AH GETS the {3} applied to letter s only since i didnt group eggs. see below
>>> 
>>> regex = re.compile(r'eggs{3}(rats)*(ranch)+')
>>> message = 'i want to go to sssranch'
>>> mo = regex.search(message)
>>> mo.group()
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    mo.group()
AttributeError: 'NoneType' object has no attribute 'group'
>>> #JKKKKK it needs to have egg then 3 s. SEE NOW FOR REAL
>>> 
>>> 
>>> regex = re.compile(r'eggs{3}(rats)*(ranch)+')
>>> message = 'i want to go to eggsssranch'
>>> mo = regex.search(message)
>>> mo.group()
'eggsssranch'
>>> # YEAAAA
>>> 
>>> # more realistic application for phone numbers
>>> 
>>> 
>>> phoneNumRegex = re.compile(r'((\d\d\d\d)*(\d\d\d)(\d\d\d\d)(,)+){3}') #this basically says find 3 comma delimited phone numbers that dont necessarily need to have the first 4 digits
>>> 
>>> message = 'I want to eat 09176545598,6635579,09182245567, and some chicken joy'
>>> mo = phoneNumRegex.search(message)
>>> mo.group()
'09176545598,6635579,09182245567,'
>>> #NICEEEE
>>> 
>>> 
>>> # if you want a range rather than a specific number of repetitions put two values within the curly brackets separated by a comma like {3,5} which basically means min max
>>> 
>>> #example
>>> 
>>> 
>>> 
>>> HaRegex = re.compile(r'(Ha){3,5}')
>>> message = 'He said "HaHaHaHa"'
>>> mo = HaRegex.search(message)
>>> mo.group()
'HaHaHaHa'
>>> # if HA is more than 5, it will match only til the 5th
>>> 
>>> message = 'He said "HaHaHaHaHaHaHa"'
>>> mo = HaRegex.search(message)
>>> mo.group()
'HaHaHaHaHa'
>>> # see kek
>>> #by default, python does greedy matches for regex ranges meaning if you putn {3,5}, it will try to reach the 5th as long as it can match til the fifth.See xample below
>>> 
>>> digitRegex = re.compile(r'(\d){3,5}')
>>> digitRegex.search('12345')
<re.Match object; span=(0, 5), match='12345'>
>>> # see that it matches til 5 even if it could do 123 instead
>>> 
>>> # if you want to do nongreedy matching, put a ? after the curly brackets
>>> 
>>> digitRegex = re.compile(r'(\d){3,5}?')
>>> digit.Regex.search('12345')
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    digit.Regex.search('12345')
NameError: name 'digit' is not defined
>>> #OOPS
>>> #sorry kek
>>> 
>>> digitRegex = re.compile(r'(\d){3,5}?')
>>> digitRegex.search('12345')
<re.Match object; span=(0, 3), match='123'>
>>> #see now it matches 123