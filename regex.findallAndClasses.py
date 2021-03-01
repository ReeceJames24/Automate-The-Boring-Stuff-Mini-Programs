Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #findall() and cahracter classes
>>> 
>>> 
>>> #note that search() method returns a match object which is why you need to do the variable.group() to show the result
>>> #MEANWHILE, findall() method returns a list of strings so you dont need to do the variable.group() anymore
>>> 
>>> #see example below
>>> 
>>> message = 'i want to eat 0917-898-6652, 0919-774-5539, and also 0911-512-3319'
>>> import re
>>> phoneNumRegex = re.compile(r'\d\d\d\d-\d\d\d-\d\d\d\d')
>>> phoneNumRegex.search(message)
<re.Match object; span=(14, 27), match='0917-898-6652'>
>>> # see it returns a matched object thats why i do the mo variable
>>> mo = phoneNumRegex.search(message)
>>> mo.group()
'0917-898-6652'
>>> # see
>>> 
>>> #for findall() you dont need to do that
>>> 
>>> phoneNumRegex.findall()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    phoneNumRegex.findall()
TypeError: findall() missing required argument 'string' (pos 1)
>>> #OOPS
>>> 
>>> phoneNumRegex.findall(message)
['0917-898-6652', '0919-774-5539', '0911-512-3319']
>>> #see
>>> 
>>> 
>>> #NOTE THAT this returning of a list of strings is how the findall() method works ONLY if theres no groupings
>>> # if you include groups in your regex object, then the findall method will return a LIST OF TUPLES OF STRINGS. see example
>>> 
>>> phoneNumRegex = re.compile(r'(\d\d\d\d)-\d\d\d-\d\d\d\d)
			   
SyntaxError: EOL while scanning string literal
>>> #OOOPS
>>> phoneNumRegex = re.compile(r'(\d\d\d\d)-\d\d\d-\d\d\d\d')
>>> message = 'i want to eat 0917-898-6652, 0919-774-5539, and also 0911-512-3319'
>>> phoneNumRegex.findall(message)
['0917', '0919', '0911']
>>> #OOPS WRONG
>>> phoneNumRegex = re.compile(r'(\d\d\d\d)-(\d\d\d-\d\d\d\d)')
>>> message = 'i want to eat 0917-898-6652, 0919-774-5539, and also 0911-512-3319'
>>> phoneNumRegex.findall(message)
[('0917', '898-6652'), ('0919', '774-5539'), ('0911', '512-3319')]
>>> #THERE SEE it gives a list of tuples of strings of the groupings in the refex object
>>> #groupings are in ordr so for example if you do a grouping that covers the whole string, that would be the first geroup and any subsequent groups would be those within that major gorup. see example
>>> 
>>>  phoneNumRegex = re.compile(r'((\d\d\d\d)-(\d\d\d-\d\d\d\d))')
 
SyntaxError: unexpected indent
>>> #OOPS
>>> 
>>> phoneNumRegex = re.compile(r'((\d\d\d\d)-(\d\d\d-\d\d\d\d))')
>>> 

>>> 
>>> 
>>> #using pipes
>>> #piped are used to mean or. see example
>>> 
>>> kekRegex = re.compile(r'nice(a|b|c|d|)')
>>> message = 'niceb'
>>> kekRegex.search(message)
<re.Match object; span=(0, 5), match='niceb'>
>>> #nice
>>> 
>>> #shorthand character classes
>>> # \d - digit
>>> #\D - not digit
>>> # \w - any numeric digit, letter, or underscore
>>> # \W - any that isnt w
>>> # \s - any space, tab, or newline character
>>> # \S - opposite of s
>>> 

>>> lyrics = '''12 drummers drumming, 11 pipers piping
10 lords a leaping, 9 ladies dancing, 8 maids a milking
7 swans a swimming, 6 geese a laying, 5 gold rings
4 calling birds, 3 French hens
2 turtle doves and 1 partridge in a pear tree'''
>>> numRegex = re.compile(r'\d+\s\w*')
>>> numRegex.search(lyrics)
<re.Match object; span=(0, 11), match='12 drummers'>
>>> #NICE
>>> numRegex.findall(lyrics)
['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 gold', '4 calling', '3 French', '2 turtle', '1 partridge']
>>> 
>>> 
>>> #creating your own character classes!!
>>> # use square brackets. see example below

>>> vowelRegex = re.compile('[aeiouAEIOU]')
>>> vowelRegex.findall('Robocop eats baby food')
['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o']
>>> # thats an easier way of doing re.compile(r'(a|e|i|o|u|A|E|I|O|U)')
>>> 
>>> #extra example
>>> 
>>> vowelRegex = re.compile(r'[aeiouAEIOU]{2}') #means oyu want it to find only 2 consecutive vowels
>>> vowelRegex.findall('Robocop eats baby food')
['ea', 'oo']
>>> #nice

>>> 
>>> #a caret ^ negates your pattern. see example
>>> 
>>> consonantsRegex = re.compile('[^aeiouAEIOU]')
>>> consonantsRegex.findall('Robocop eats baby food')
['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd']
>>> 