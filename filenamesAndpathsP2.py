Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> #absolute and relative file paths
>>> 
>>> #absolute file paths are those files that include the root
>>> # like this /Users/chummi/Desktop/PyPrac/eggs.py
>>> 
>>> #relative file paths are those that don't include the root path
>>> 
>>> #like this eggs.py (assumed to be in whatever your cwd is)
>>> #also like this /Pyprac/eggs.py (Pyprac folder is assumed to be in whatever your cwd is )
>>> 
>>> 
>>> #os.path.abspath() will return a relative file path you indicate as an absolute file path
>>> #exmaple
>>> import os
>>> os.path.abspath('infinite_loop.py')
'/Users/chummi/infinite_loop.py'
>>> # it automaticallly applies your cwd to make it into an absolute root path
>>> 
>>> #os.path.isabs() is basically boolean on your path to check if it is an absolute poth
>>> #this is used to see if the first folder of a file path is actually the root folder already
>>> #example
>>> os.path.isabs('/Desktop/PyPrac/infinite_loop.py')
True
>>> os.path.isabs('/PyPrac/infinite_loop.py')
True
>>> os.path.isabs('infinite_loop.py')
False
>>> #hmm im a bit confused here
>>> 
>>> #os.path.relpath gives you a relative path between 2 paths you input
>>> #example
>>> 
>>> os.getcwd()
'/Users/chummi'
>>> os.path.relpath('infinite_loop.py', '/Users/chummi')
'infinite_loop.py'
>>> # see
>>> 
>>> #another example
>>> os.path.relpath('/Desktop/PyPrac/infinite_loop.py
		
SyntaxError: EOL while scanning string literal
>>> os.path.relpath('/Desktop/PyPrac/infinite_loop.py', '/Users/chummi/)
		
SyntaxError: EOL while scanning string literal
>>> #OOPS
>>> os.path.relpath('/Desktop/PyPrac/infinite_loop.py', '/Users/chummi/')
'../../Desktop/PyPrac/infinite_loop.py'
>>> 
>>> 
>>> #NOTE: check al sweigart video 30 to restudy ../ and ./ for relative paths
>>> 
>>> # to reexplain os.path.relpath, it basically gives you the realtive path of the first string, assuming that the second string is your current working directory
>>> 
>>> os.path.join('User','chummi','Desktop','PyPrac','infinite)loop.py
	     
SyntaxError: EOL while scanning string literal
>>> os.path.join('User','chummi','Desktop','PyPrac','infinite_loop.py')
'User/chummi/Desktop/PyPrac/infinite_loop.py'
>>> os.path.relpath('User/chummi/Desktop/PyPrac/infinite_loop.py', '/User/chummi/')
'../../Users/chummi/User/chummi/Desktop/PyPrac/infinite_loop.py'
>>> #OOPS
>>> 
>>> s.path.relpath('/User/chummi/Desktop/PyPrac/infinite_loop.py', '/User/chummi/')
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    s.path.relpath('/User/chummi/Desktop/PyPrac/infinite_loop.py', '/User/chummi/')
NameError: name 's' is not defined
>>> #OOPS
>>> 
>>> os.path.relpath('/User/chummi/Desktop/PyPrac/infinite_loop.py', '/User/chummi/')
'Desktop/PyPrac/infinite_loop.py'
>>> #THERE WE GO thats the relpath of the first string assuming the second string is your root path
>>> 

>>> #os.path.dirname() returns everything except for the last file name (or foled if your path string ends in a folder) and os.path.basename() returns only the last file name/folder name
>>> 
>>> #example
>>> 
>>> os.path.dirname('/User/chummi/Desktop/PyPrac/infinite_loop.py')
'/User/chummi/Desktop/PyPrac'
>>> os.path.basename('/User/chummi/Desktop/PyPrac/infinite_loop.py')
'infinite_loop.py'
>>> #SEE NICE
>>> 
>>> #os.path.exists() is used to see if the path and filename actually exists
>>> 
>>> #example
>>> os.path.exists('/User/chummi/Desktop/PyPrac/infinite_loop.py')
False
>>> #hmm i wonder why lets check the cwd
>>> os.getcwd()
'/Users/chummi'
>>> #JK I GET IT I PUT USER INSTEAD OF USERS KEK
>>> 
>>> #lets try again!
>>> 
>>> os.path.exists('/Users/chummi/Desktop/PyPrac/infinite_loop.py')
True
>>> #NICE
>>> 
>>> #os.path.isfile() checks if its a file and os.path.isdir() cheks if its a directory/folder
>>> 
>>> os.path.isfile('/Users/chummi/Desktop/PyPrac/infinite_loop.py')
True
>>> os.path.isfile('/Users/chummi/Desktop/Pyprac')
False
>>> #NICE
>>> os.path.isdir('/Users/chummi/Desktop/PyPrac')
True
>>> #NICE
>>> 
>>> #os.path.getsize() returns the size of oyur file in bytes
>>> 
>>> os.path.getsize('/Users/chummi/Desktop/PyPrac/infinite_loop.py')
75
>>> #NICE
>>> 
>>> #os.listdir() returns all the files in your specified directory/folder
>>> 
>>> os.listdir('/Users/chummi/Desktop/PyPrac')
['string.methods.py', 'regex.groupsAndPipes.py', 'phonenumber.identifier.py', 'shebangline.py', 'regex.Repetition.py', 'filenamesAndpathsP2.py', 'Program1.py', 'Lists.py', '.DS_Store', 'regex.GroupNOtes.py', 'characterCount.py', 'Advanced.StringSyntax.py', 'regex.Verbose.py', 'try.except.py', 'methods.py', 'regex.submethod.py', 'guessing.numbergame.py', 'def.py', 'sumofallnumbersfrom0to100.py', 'numberIdentifier.regex.py', 'fivetimes.py', 'infinite_loop.py', 'data.structures.tictactoe.py', 'assignment.swap.py', 'guess.the.number.py', 'NumandEmailExtractor.py', 'regex.findallAndClasses.py', 'def.with.parameter.py', 'regex.dot-star.py', 'numberIdentifier.fromMessage.py', 'regex.submethodP2.py', 'augmented.operators.py', 'multiple.assignments.py', 'Screen Shot 2020-09-18 at 10.59.46 PM.png', 'dictionaries.py', 'input.validation.py', 'while_continue_sample.py', 'NoneValue.py', 'if_elif_boolean_test.py', 'runUsingTerminal.py', 'for.loops.w:.range,list,len.py', 'pyperclipnotes.py', 'Mutable.Immutable.py', 'string.formatting:interpolation.py', 'sys.exit.py', 'TEST.numberIdentifier.regex.py', 'regex.groups.py', 'autoclicker.py', 'filenameAndpathsP1.py', 'def.and.return.py', 'shebang.test.py', 'regex.caseInsensitive.py', 'while_test.py', 'def.mutable.py']
>>> #NCIEEE
>>> 

>>> 
========== RESTART: /Users/chummi/Desktop/PyPrac/directoryByteSize.py ==========
Traceback (most recent call last):
  File "/Users/chummi/Desktop/PyPrac/directoryByteSize.py", line 14, in <module>
    print(str(directoryName) + ' has' + totalByteSize + ' bytes.')
TypeError: can only concatenate str (not "int") to str
>>> 
========== RESTART: /Users/chummi/Desktop/PyPrac/directoryByteSize.py ==========
PyPrac has184590 bytes.
>>> 
========== RESTART: /Users/chummi/Desktop/PyPrac/directoryByteSize.py ==========
PyPrac has 184591 bytes.
>>> 
========== RESTART: /Users/chummi/Desktop/PyPrac/directoryByteSize.py ==========
Input absolute path of directory
/Users/chummi/Desktop/PyPrac
PyPrac has 184609 bytes.
>>> 
========== RESTART: /Users/chummi/Desktop/PyPrac/directoryByteSize.py ==========
Input absolute path of directory
nice
Traceback (most recent call last):
  File "/Users/chummi/Desktop/PyPrac/directoryByteSize.py", line 9, in <module>
    for file in os.listdir(directoryAbsPath):
FileNotFoundError: [Errno 2] No such file or directory: 'nice'
>>> 
========== RESTART: /Users/chummi/Desktop/PyPrac/directoryByteSize.py ==========
Input absolute path of directory
/Users/chummi/Desktop/JOJO
JOJO has 6869861 bytes.
>>> 