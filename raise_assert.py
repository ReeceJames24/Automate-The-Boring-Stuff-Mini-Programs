Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 

>>> #DEBUGGING
>>> 
>>> #raise and assert statements
>>> 
============== RESTART: /Users/chummi/Desktop/PyPrac/boxprinter.py =============
OOOOOOOO
O      O
O      O
O      O
O      O
O      O
OOOOOOOO
>>> 
============== RESTART: /Users/chummi/Desktop/PyPrac/boxprinter.py =============
OOOOOOOO
O      O
O      O
O      O
O      O
O      O
OOOOOOOO
>>> 
============== RESTART: /Users/chummi/Desktop/PyPrac/boxprinter.py =============
Traceback (most recent call last):
  File "/Users/chummi/Desktop/PyPrac/boxprinter.py", line 29, in <module>
    boxprinter('OO', 7, 8)
  File "/Users/chummi/Desktop/PyPrac/boxprinter.py", line 17, in boxprinter
    raise Exception('"symbol" needs to be exactly one character') #this will return a custom error statement for this custom error you determined
Exception: "symbol" needs to be exactly one character
>>> 

>>> 
>>> #traceback.format_exc() function
>>> #this is used to convert the traceback/callstack statement during errors into text
>>> 
>>> #example of how to use this traceback to create a a text log for your errors
>>> 
>>> import traceback
>>> try:
	raise Exception('this is the error message lol')
except:
	errorFile = open('/Users/chummi/Desktop/Cheken/errorlog.txt', 'a')
	errorFile.write(traceback.format_exc())
	errorFile.close()
	print('Error stack call has been copied to errorlog.txt')

	
119
Error stack call has been copied to errorlog.txt
>>> #nice let's see if its there
>>> errorFile = open('/Users/chummi/Desktop/Cheken/errorlog.txt')
>>> errorFile.read()
'Traceback (most recent call last):\n  File "<pyshell#20>", line 2, in <module>\nException: this is the error message lol\n'
>>> #NICE
>>> 
>>> errorFile.close()
>>> 
>>> 

>>> 
>>> #assertions and the assert statement
>>> # these are sanity chekcs to ensure that your code isnt doing anything obviously wrong
>>> #done using assert statements
>>> # if it results to false, you receive an assertion error
>>> assert False, 'ERROR LOLLL'
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    assert False, 'ERROR LOLLL'
AssertionError: ERROR LOLLL
>>> # this is what its oging to look like. That one resulted to an immediate error since False will always be equal to False
>>> 

>>> #unlike try and except, your program will crash as soon as the condition isnt met which is good cause it will be easy for you to trace the error
>>> 
>>> # NOTE on raise exception vs assert
>>> Print('''Assertions can be disabled with the -O flag when starting Python. For this reason, use assertions only for sanity-checking, not for checking that is part of your program logic.

Besides this, there is of course the difference that assertions raise AssertionError, which you really shouldn't catch. When you raise an exception, you can make the type of the exception appropriate to the error and catch it later.''')
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    Print('''Assertions can be disabled with the -O flag when starting Python. For this reason, use assertions only for sanity-checking, not for checking that is part of your program logic.
NameError: name 'Print' is not defined
>>> print('''Assertions can be disabled with the -O flag when starting Python. For this reason, use assertions only for sanity-checking, not for checking that is part of your program logic.

Besides this, there is of course the difference that assertions raise AssertionError, which you really shouldn't catch. When you raise an exception, you can make the type of the exception appropriate to the error and catch it later.''')
Assertions can be disabled with the -O flag when starting Python. For this reason, use assertions only for sanity-checking, not for checking that is part of your program logic.

Besides this, there is of course the difference that assertions raise AssertionError, which you really shouldn't catch. When you raise an exception, you can make the type of the exception appropriate to the error and catch it later.
>>> 
>>> 

>>> #SEE INTERSECITON LIGHTS EXAMPLE