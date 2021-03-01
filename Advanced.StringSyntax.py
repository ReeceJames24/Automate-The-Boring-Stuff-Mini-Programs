Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 

>>> # Advanced String Syntax
>>> 
>>> # you can't use the single quote within the quotation marks of the string. see what i mean below
>>> 
>>> 'That is Alice's Cat'
SyntaxError: invalid syntax
>>> #one work around is to use double quotes but a better solution is to use the escape character \ (recall regex)
>>> 
>>> 'That is Alice\'s Cat'
"That is Alice's Cat"
>>> 
>>> 
>>> # to print out text strings in separate lines
>>> 
>>> print('Hello There!\nHow Are You?\nI\'m Fine')
Hello There!
How Are You?
I'm Fine
>>> # this is regex!!!
>>> 
>>> 
>>> # raw string - add r to the start of the string
>>> # it allows the string to come out as it is (disregards escape characters)
>>> # useful when you have a string with lots of backslashes
>>> # example:
>>> 
>>> 
>>> r'Hello'
'Hello'
>>> print(r'that is carol\'s cat')
that is carol\'s cat
>>> # see it includes the backslash
>>> 
>>> 
>>> # Multiline Strings with Triple Quotes
>>> # they start and end with triple quotes or double quotes
>>> # they start and end with triple quotes or double quotes
>>> # use them when you want to create multiline strings easily
>>> 
>>> #example
>>> 
>>> print(""" Dear Alice,
Eve's Cat has been arrested for catnapping, cat burglary,
and extortion.
Sincerely,
Bob.""")
 Dear Alice,
Eve's Cat has been arrested for catnapping, cat burglary,
and extortion.
Sincerely,
Bob.
>>> # it allows you to breake the line rules and oyou are able to adjust the lining yourself
>>> # use the triple quotes when you assign an incredibly large text string with lots of spaces between paragraphs (like text from a page of a novel) to a variable
>>> 
>>> 
>>> # note that strings are considered list-like data meaning indexes, slices, and the in and not in operators all work on strings
>>> 
>>> #see example below
>>> 
>>> "Hello World"
'Hello World'
>>> spam = "Hello World"
>>> spam[0]
'H'
>>> spam[-1]
'd'
>>> spam[1:5]
'ello'
>>> "Hello" in spam
True
>>> 'eggs' in spam
False
>>> # note that the oeprators are case sensitive. See example below
>>> 'HELLo' in spam
False
>>> 