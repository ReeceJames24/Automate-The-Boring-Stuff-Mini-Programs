Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # VERBOSE MODE
>>> 
>>> import re
>>> 
>>> #sometimes when you look back to your regex files, it gets a bit confusing to rememmeber what the patterns were for.
>>> #to make it more readeable, we can switch to verbose mode
>>> #in verbose mode, you dont have to use \n to create new lines
>>> # therefore u can split up your regex object with each of their own comments for better readability
>>> 
>>> #see example for the number finder regex we did before
>>> 
>>> numRegex = re.compile(r'\d\d\d\d-\d\d\d-\d\d\d\d')
>>> # see its a bit confusing and we only have space to put 1 long comment since its just 1 line
>>> #heres how to make it more readable with the verbose mode
>>> 
>>> numRegex = re.compile(r'''
\d\d\d\d  #first 4 digits
-       # first dash
\d\d\d  # next 3 digits
-       # second dash
\d\d\d\d''', re.VERBOSE) # final 4 digits
>>> #SEE ITS WAY EASIER TO READ

>>> 
>>> 
>>> #MULTIPLE 2nd ARGUMENTS FOR COMPILE FUNCTION
>>> 
>>> #if you want to use verbose, ignorecase, and dotall at once, u use the pipe to separate them
>>> # NOTE THATTHIS SYNTAX IS SPECIFICALLY FOR COMPILE FUNCTION!! DONT USE ON OTHERS
>>> 
>>> #EXAMPLE
>>> 
>>> numRegex = re.compile(r'''
\d\d\d\d  #first 4 digits
-       # first dash
\d\d\d  # next 3 digits
-       # second dash
\d\d\d\d''', re.VERBOSE | re.I | re.DOTALL)
>>> #thats how to do it SPECIFICALLY for this compile function
>>> 