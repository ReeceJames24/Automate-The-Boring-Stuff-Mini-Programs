Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #LOGGING
>>> 
>>> #here's the set-up for logging in python. Try to put it somehwere at the start of you programs
>>> 
>>> import logging
>>> logging.basicConfig(level=logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(messages)s')
>>> # THIS IS THE BASIC SETUP

>>> # lets try to do logging for a buggy factorial program
>>> #checkout the factorial.py file
>>> 
============== RESTART: /Users/chummi/Desktop/PyPrac/factorial.py ==============
0
>>> # see its buggy for some reason factorial of 5 cant be 0
>>> 
>>> 
============== RESTART: /Users/chummi/Desktop/PyPrac/factorial.py ==============
--- Logging error ---
Traceback (most recent call last):
  File "/opt/anaconda3/lib/python3.8/logging/__init__.py", line 436, in format
    return self._format(record)
  File "/opt/anaconda3/lib/python3.8/logging/__init__.py", line 432, in _format
    return self._fmt % record.__dict__
KeyError: 'messages'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/opt/anaconda3/lib/python3.8/logging/__init__.py", line 1081, in emit
    msg = self.format(record)
  File "/opt/anaconda3/lib/python3.8/logging/__init__.py", line 925, in format
    return fmt.format(record)
  File "/opt/anaconda3/lib/python3.8/logging/__init__.py", line 667, in format
    s = self.formatMessage(record)
  File "/opt/anaconda3/lib/python3.8/logging/__init__.py", line 636, in formatMessage
    return self._style.format(record)
  File "/opt/anaconda3/lib/python3.8/logging/__init__.py", line 438, in format
    raise ValueError('Formatting field not found in record: %s' % e)
ValueError: Formatting field not found in record: 'messages'
Call stack:
  File "<string>", line 1, in <module>
  File "/opt/anaconda3/lib/python3.8/idlelib/run.py", line 155, in main
    ret = method(*args, **kwargs)
  File "/opt/anaconda3/lib/python3.8/idlelib/run.py", line 548, in runcode
    exec(code, self.locals)
  File "/Users/chummi/Desktop/PyPrac/factorial.py", line 4, in <module>
    logging.debug('Start of Program')
Message: 'Start of Program'
Arguments: ()
The factorial of 5 is:
Traceback (most recent call last):
  File "/Users/chummi/Desktop/PyPrac/factorial.py", line 17, in <module>
    print(factorial(5))
  File "/Users/chummi/Desktop/PyPrac/factorial.py", line 6, in factorial
    logging.debug('Start of factorial(%n)' % (n))
ValueError: unsupported format character 'n' (0x6e) at index 20
>>> 
>>> 
>>> 
>>> #OOPS let us redo that
>>> 
>>> 
>>> 
============== RESTART: /Users/chummi/Desktop/PyPrac/factorial.py ==============
2020-10-09 14:37:40,428 - DEBUG - Start of Program
The factorial of 5 is:
Traceback (most recent call last):
  File "/Users/chummi/Desktop/PyPrac/factorial.py", line 17, in <module>
    print(factorial(5))
  File "/Users/chummi/Desktop/PyPrac/factorial.py", line 6, in factorial
    logging.debug('Start of factorial(%n)' % (n))
ValueError: unsupported format character 'n' (0x6e) at index 20
>>> 
============== RESTART: /Users/chummi/Desktop/PyPrac/factorial.py ==============
2020-10-09 14:40:12,491 - DEBUG - Start of Program
The factorial of 5 is:
Traceback (most recent call last):
  File "/Users/chummi/Desktop/PyPrac/factorial.py", line 17, in <module>
    print(factorial(5))
  File "/Users/chummi/Desktop/PyPrac/factorial.py", line 6, in factorial
    logging.debug('Start of factorial(%n)' % (n))
ValueError: unsupported format character 'n' (0x6e) at index 20
>>> 
============== RESTART: /Users/chummi/Desktop/PyPrac/factorial.py ==============
2020-10-09 14:43:15,989 - DEBUG - Start of Program
The factorial of 5 is:
2020-10-09 14:43:16,127 - DEBUG - Start of factorial(5)
2020-10-09 14:43:16,152 - DEBUG - i is 0 and total is 0
2020-10-09 14:43:16,184 - DEBUG - i is 1 and total is 0
2020-10-09 14:43:16,236 - DEBUG - i is 2 and total is 0
2020-10-09 14:43:16,259 - DEBUG - i is 3 and total is 0
2020-10-09 14:43:16,282 - DEBUG - i is 4 and total is 0
2020-10-09 14:43:16,333 - DEBUG - i is 5 and total is 0
2020-10-09 14:43:16,365 - DEBUG - Return value is 0
0
2020-10-09 14:43:16,499 - DEBUG - End of program
>>> #NICE FINALLY
>>> 
>>> 
>>> #so here we can see that its wrong starting at the second iteration
>>> # we can see now that theres soemthing wrong with our code.
>>> # since we the first iteration results to 0, it then multiplies that to the next iteration which is 0 which would still lead to 0
>>> # we need to change the range to not inclue 0 for i
>>> # lets change it now from for i in range(n + 1) to for i in range (1, n + 1)
>>> 
============== RESTART: /Users/chummi/Desktop/PyPrac/factorial.py ==============
2020-10-09 14:48:31,262 - DEBUG - Start of Program
The factorial of 5 is:
2020-10-09 14:48:31,582 - DEBUG - Start of factorial(5)
2020-10-09 14:48:31,657 - DEBUG - i is 1 and total is 1
2020-10-09 14:48:31,695 - DEBUG - i is 2 and total is 2
2020-10-09 14:48:31,721 - DEBUG - i is 3 and total is 6
2020-10-09 14:48:31,758 - DEBUG - i is 4 and total is 24
2020-10-09 14:48:31,795 - DEBUG - i is 5 and total is 120
2020-10-09 14:48:31,821 - DEBUG - Return value is 120
120
2020-10-09 14:48:31,995 - DEBUG - End of program
>>> # SEE NOW WE GOOD
>>> 
>>> #now if we want to turn off these debug statements without manually deleting each, we simply type
>>> #   #logging.disable(logging.CRITICAL)
>>> # place this at the start
>>> # if you want to reactivate the debug, simply put a # to turn that line into a comment :)
>>> 
>>> 

>>> 

>>> #LOG LEVELS
>>> # debug(lowest), info, warning, error, critical (highest)
>>> 
>>> #for the program, we did logging.debug which is the lowest level, you can simply replace debug() with info, warning, error, or critical ot change levels
>>> 
>>>  #logging.disable(logging.CRITICAL) the critical here means to disable all log emssages at critical level and lower (basically all logs)
>>> 
>>> # this allows you to be able to hide the logs of  only the levels you want to hide :)
>>> 
>>> #NOTE
>>> 
>>> 
>>> #if you dont want the logging messages to show up when you run the progam, input a filename to send the log emssages to at the start of the the logging set up code
>>> 
>>> #so instead of this
>>> #logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
>>> 
>>> #put this
>>> 
>>> #logging.basicConfig(filename='ProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
>>> 
>>> #make sure to indicate absolute path if you neeed it at a specific directory!!