Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 

>>> 
>>> # STRING METHODS
>>> 
>>> 
>>> 
>>> 
>>> # recall that strings are immutable and thus return new values each time and cannot be edited in place
>>> 
>>> spam = "Hello World'
SyntaxError: EOL while scanning string literal
>>> spam = 'Hello World'
>>> spam
'Hello World'
>>> spam.upper()
'HELLO WORLD'
>>> #note that spam itself hasnt actually been changed since its immutable
>>> spam
'Hello World'
>>> #if oyu want to convert spam you need to assign
>>> spam = spam.upper()
>>> spam
'HELLO WORLD'
>>> spam.lower()
'hello world'
>>> spam = spam.lower()
>>> spa
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    spa
NameError: name 'spa' is not defined
>>> spam
'hello world'
>>> 
>>> #you can use the upper and lower methods for inputs
>>> 
>>> answer = input()
yes
>>> if answer == 'yes':
	print('Playing again')

	
Playing again
>>> #however if the user types in "YES", it wont work
>>> answer = input()
YES
>>> if answer == 'yes':
	print('Playing again')

	
>>> # see its false
>>> # to address this
>>> 
>>> if answer.lower() == 'yes':
	print('Playing again')

	
Playing again
>>> # there we go nice
>>> 
>>> 
>>> #isupper and islower methods return boolean vales
>>> 
>>> spam = 'Hello world'
>>> spam.islower()
False
>>> # false cause H is capital
>>> 
>>> spam = spam.lower()
>>> spam
'hello world'
>>> spam.islower()
True
>>> 'Hello'.upper().isupper()
True
>>> # stacking method calls
>>> 
>>> #other methods
>>> # isalpha() - letters only
>>> # isalnum() - letters and numbers only
>>> # isdecimal() - numbers only
>>> # issapce() - whitespace only
>>> # istitle() - titlecase only
>>> 
>>> 'Hello world'.isspace()
False
>>> 'Hello world'[5].isspace()
True
>>> # true because you get the indx of the space withint the string
>>> 
>>> # starswith() method
>>> 
>>> # oh and endswith method also
>>> 
>>> "Hello world".startswith('Hello')
True
>>> 'Hello world'.startswith('H')
True
>>> 'Hello world'.startswith('Hello world'[0])
True
>>> 'Hello world'.endswith('d')
True
>>> 'Hello world'.endswith('Hell')
False
>>> #join method
>>> 
>>> ''.join(['cats', 'rats', 'bats'])
'catsratsbats'
>>> ','.join(['cats', 'rats', 'bats'])
'cats,rats,bats'
>>> '\n\n'.join(['cats', 'rats', 'bats'])
'cats\n\nrats\n\nbats'
>>> # \n is new line. you will see the effects when you pass it to a print function

>>> print('\n\n'.join(['cats', 'rats', 'bats']))
cats

rats

bats
>>> # nice
>>> 
>>> #split(method)
>>> 
>>> 'My Name Is'.split()
['My', 'Name', 'Is']
>>> # splits them by whitespaces
>>> 
>>> 'My Name Is'.split('x')
['My Name Is']
>>> # doesnt work cause theres no 'x' in the string
>>> 
>>> 'Xeggs Xa Xday'.split('X')
['', 'eggs ', 'a ', 'day']
>>> # it splits it now by the Xs
>>> # it splits it now by the Xs
>>> 
>>> 

>>> #rjust() and ljust() methods add whitespaces (by default) to reach number of characters you pass into the methods. see example below
>>> 
>>> 'Hello'.rjust(10)
'     Hello'
>>> spam = 'Hello'.rjust(10)
>>> spam
'     Hello'
>>> len(spam)
10
>>> # see
>>> 
>>> spam = 'Hello'.ljust(10)
>>> spam
'Hello     '
>>> len(spam)
10
>>> # nice
>>> 
>>> # if you want to specify what to add
>>> spam = 'Hello'.rjust(10, '*')
>>> spam
'*****Hello'
>>> len(spam)
10
>>> # nice

>>> 
>>> #center() method is similar to rjust and ljust but justifies your text tot he center instead
>>> 
>>> spam = 'Hello'.center(20, '=')
>>> spam
'=======Hello========'
>>> len(spam)
20
>>> #nice
>>> 

>>> 
>>> #strip(), rstrip(), lstrip() methods are used to remove whitespaces or specified characters
>>> 
>>> 
>>> spam = 'Hello'.rjust(10)
>>> spam
>>> spam
'     Hello'
>>> spam.strip()
'Hello'
>>> #removes white space from either side of the string
>>> #removes white space from either side of the string
>>> #note that what i did above doesnt change spam itself since its immutable
>>> spam
'     Hello'
>>> # if you want to change it,
>>> 
>>> spam = spam.strip()
>>> spam
'Hello'
>>> '       x         '.strip()
'x'
>>> '       x         '.lstrip()
'x         '
>>> '       x         '.rstrip()
'       x'
>>> 
>>> 
>>> SpamSpamBaconSpamEggsSpamSpam.strip('ampS')
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    SpamSpamBaconSpamEggsSpamSpam.strip('ampS')
NameError: name 'SpamSpamBaconSpamEggsSpamSpam' is not defined
>>> #oops
>>> 'SpamSpamBaconSpamEggsSpamSpam'.strip('ampS')
'BaconSpamEggs'
>>> #note that theres still spam in the middle of the output because the method stopped on both sides once it reached "Bacon" on the left and "Eggs" on the right
>>> 
>>> 
>>> 
>>> # replace() method
>>> 
>>> spam = 'Hello there!'
>>> spam = spam.replace('e', '69')
>>> spam
'H69llo th69r69!'
>>> #nice
>>> 
>>> 
i
>>> import pyperclip
>>> 
>>> #copy and past functions
>>> 
>>> pyperclip.copy('Nice')
>>> Nice
Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    Nice
NameError: name 'Nice' is not defined
>>> pyperclip.paste()
'Nice'
>>> #nice
>>> # useful for when you ened to copy a long ass string like a whole essay