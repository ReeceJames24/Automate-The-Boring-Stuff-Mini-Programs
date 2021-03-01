Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # caret is used to signify that the pattern should be found at the start of the string
>>> 

>>> import re
>>> caretRegex = re.compile(r'^Hello')
>>> caretRegex.search('Hello there boi')
<re.Match object; span=(0, 5), match='Hello'>
>>> caretRegex.search('He said Hello')
>>> # it doesnt work if the hello isnt at the start of the string
>>> 
>>> caretRegex.search('He said Hello') == None
True
>>> # see
>>> #use the $ to signify that it should be the end of the string
>>> 
>>> Regex = re.compile(r'world$')
>>> Regex.search('Hello world')
<re.Match object; span=(6, 11), match='world'>
>>> # if you use both ^ and $ it means you want it to match the entire string
>>> 
>>> # the wildcard . character is used to signify any single character
>>> 
>>> Regex = re.compile(r'.at') #means match any character followed by at
>>> text = 'The fat cat in the hat sat on the flat mat'
>>> Regex.findall(text)
['fat', 'cat', 'hat', 'sat', 'lat', 'mat']
>>> # note that it matched lat and not flat since . says only one any character. if you want to match flat, you can add a + or a range
>>> 
>>> Regex = re.compile(r'.{1,2}at')
>>> text = 'The fat cat in the hat sat on the flat mat'
>>> Regex.findall(text)
[' fat', ' cat', ' hat', ' sat', 'flat', ' mat']
>>> #there we goo
>>> # it includes whitespaces tho so the others ow have spaces before the 3 letter word
>>> 
>>> 
>>> 
>>> #the dot-star combination means match ANYTHING AT ALL (.*)
>>> 
>>> 
>>> #example
>>> 
>>> 
>>> text = 'First Name: Chummi Last Name: Crisologo'
>>> nameRegex = re.compile(r'First Name: .* Last Name: .*)
		       
SyntaxError: EOL while scanning string literal
>>> nameRegex = re.compile(r'First Name: .* Last Name: .*')
>>> nameRegex.findall(text)
['First Name: Chummi Last Name: Crisologo']
>>> #if you want only the first and last names to be matched, use groupings
>>> nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
>>> nameRegex.findall(text)
[('Chummi', 'Crisologo')]
>>> # note tho that it will return a list of tuples of strings
>>> # note also that it will automatically match as much as possible since its greedy by default
>>> 
>>> #comparison of greedy and nongreedy use of dot-star
>>> 
>>> text = '<to serve humans> for dinner>'
>>> Greedy = re.compile(r'<(.*)>')
>>> Greedy.findall(text)
['to serve humans> for dinner']
>>> # python basically goes yo the first > fits the pattern but apparently if i go forward, there is another > that will still make the pattern valid
>>> 
>>> nonGreedy = re.compile(r'<.*>?')
>>> nonGreedy.findall(text)
['<to serve humans> for dinner>']
>>> #OOOPS
>>> nonGreedy = re.compile(r'<(.*?)>')
>>> nonGreedy.findall(text)
['to serve humans']
>>> #see it only matches the first match for <>
>>> 
>>> # NOTE: dot refers to ANY CHARACTER EXCEPT NEW LINE meaning it wont match newlines. see example
>>> 
>>> eggs = 'bacon \nchicken \nnuggets'
>>> print(eggs)
bacon 
chicken 
nuggets
>>> dotstar = re.compile('r.*')
>>> dotstar.findall(eggs)
[]
>>> #OOPS
>>> dotstar.search(eggs)
>>> eggs = 'bacon \nchicken \nnuggets'
>>> dotstar.search(eggs)
>>> #wot im confused nvm
>>> #but basically if you want to refer to ANY CHARACTER INCLUDING NEW LINES
>>> # what you do is you pass a second argument in the compile function. That argument is re.DOTALL.
>>> # so your object should lookk liek this dotstar = re.compile('r.*', re.DOTALL)
>>> 
>>> 