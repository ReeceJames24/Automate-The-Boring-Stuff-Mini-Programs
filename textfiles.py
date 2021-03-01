Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 

>>> #two types of text files
>>> #Plaintext and Binary Files
>>> #Plain text files are those that are simple text
>>> #plaintext files usually end in .txt except for python scripts which end in py but are also considere plain text files
>>> 
>>> #binary files are those that store info on color, font, etc like spreadsheets word processors like ms word, etc.
>>> 
>>> 
>>> helloFile = open('/Users/chummi/Desktop/hello.txt')
>>> #that opens up the file in READ MODE. It allows you to read the file ONLY
>>> #read() method lets you see the contents of the file
>>> 
>>> helloFile.read()
'Hello World'
>>> 
>>> #lets switch to a file w text separated by lines
>>> 
>>> #nvm just edited the same file
>>> 
>>> helloFile = open('/Users/chummi/Desktop/hello.txt')
>>> helloFile.read()
'Hello World\n\nSUP RAT'
>>> # read method doesnt display newlines. use the print function to show it
>>> print(helloFile.read())

>>> 
>>> #OOPS
>>> content = helloFile.read()
>>> print(content)

>>> helloFile.read()
''
>>> helloFile = open('/Users/chummi/Desktop/hello.txt')
>>> helloFile.read()
'Hello World\n\nSUP RAT'
>>> helloFile.read()
''
>>> #I SEE i need to open it again
>>> helloFile = open('/Users/chummi/Desktop/hello.txt')
>>> print(helloFile.read())
Hello World

SUP RAT
>>> #THERE WE GO
>>> 
>>> #readlines() method returns the contents of the file in a list of string

>>> helloFile = open('/Users/chummi/Desktop/hello.txt')
>>> helloFile.readlines()
['Hello World\n', '\n', 'SUP RAT']
>>> #NICE
>>> 
>>> 
>>> #write and append mode
>>> #to activate these, add w or a respectively following a comma after the file path argument of your open function
>>> #write mode allows you to rewrite the whole text file
>>> #append mode simply adds to the current text file content
>>> 
>>> #example
>>> 
>>> helloFile = open('/Users/chummi/Desktop/hello.txt', 'w')
>>> #then u use the write method to write into the file
>>> helloFile.write('KEK')
3
>>> #dont mind the output it just shows how many bytes the file currently has
>>> helloFile.write('KOK')
3
>>> #jk how many characters you added pala
>>> helloFile.write('\nCHEKENWENGS')
12
>>> helloFile.close()
>>> #note that you can only use the read methods once meaning you need to reopen the file to read again
>>> 
>>> #check the hello file now to see if the edits i made took place
>>> #NOOICE IT WORKED
>>> 
>>> #note that if you do an open function and you put a file name that doesnt exist, python will automatically create taht file for oyu
>>> #if you put a relative file path, it will automatically apply your current working directory
>>> 
>>> #example
>>> 
>>> baconFile = open('bacon.file','w')
>>> baconFile.write('SUP DOC')
7
>>> # to check where your relative path is saved check ur cwd
>>> import os
>>> os.getcwd()
'/Users/chummi'
>>> #it will be placed there
>>> 
>>> #oops wrong bacon it should be txt lmemme redo
>>> 
>>> baconFile = open('bacon.txt', 'w')
>>> baconFile.write('yo excercise')
12
>>> baconFile.close()
>>> baconFile.open()
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    baconFile.open()
AttributeError: '_io.TextIOWrapper' object has no attribute 'open'
>>> #OOOPS
>>> baconFile = open('bacon.txt', 'w')
>>> baconFile.read()
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    baconFile.read()
io.UnsupportedOperation: not readable
>>> baconFile = open('bacon.txt', 'w')
>>> baconFile.write('yo excercise')
12
>>> baconFile.read()
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    baconFile.read()
io.UnsupportedOperation: not readable
>>> #WOT
>>> 
>>> #LETS REDO THIS
>>> 
>>> 
>>> spamFile = open('/Desktop/bacon.txt', 'w')
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    spamFile = open('/Desktop/bacon.txt', 'w')
FileNotFoundError: [Errno 2] No such file or directory: '/Desktop/bacon.txt'
>>> spamFile = open('Users/chummi/Desktop/bacon.txt', 'w')
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    spamFile = open('Users/chummi/Desktop/bacon.txt', 'w')
FileNotFoundError: [Errno 2] No such file or directory: 'Users/chummi/Desktop/bacon.txt'
>>> 
>>> #okay lets change directory
>>> 
>>> import os
>>> os.getcwd()
'/Users/chummi'
>>> os.chdir('/Users/chummi/Desktop/Cheken')
>>> os.getcwd()
'/Users/chummi/Desktop/Cheken'
>>> spamFile = open('spam.txt','w')
>>> spamFile.write('YO PLS WORK MAN')
15
>>> spamFile.close()
>>> #Nice i checked the cheken folder and it is there
>>> 
>>> #lets append
>>> 
>>> spamFile = open('spam.txt','a')
>>> spamFile.write('\n\n EYO goodjoab')
15
>>> spamFile.close()
>>> #NICE IT WORKED
>>> 

>>> #shelve module creataes a shelve file object rather than a simple text file object
>>> # this allows you to store variables and all
>>> 
>>> #you can make changes to the shelve value like a dictionary
>>> 
>>> import shelve
>>> shelveFile = shelve.open('Rat','Cat','Bat')
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    shelveFile = shelve.open('Rat','Cat','Bat')
  File "/opt/anaconda3/lib/python3.8/shelve.py", line 243, in open
    return DbfilenameShelf(filename, flag, protocol, writeback)
  File "/opt/anaconda3/lib/python3.8/shelve.py", line 227, in __init__
    Shelf.__init__(self, dbm.open(filename, flag), protocol, writeback)
  File "/opt/anaconda3/lib/python3.8/dbm/__init__.py", line 85, in open
    raise error[0]("db file doesn't exist; "
dbm.error: db file doesn't exist; use 'c' or 'n' flag to create a new db
>>> #OOOPS lets redo that

>>> 
>>> shelveFile = shelve.open('ratFile')
>>> #its gonna automatically create that shelve file object for u (ratFile)
>>> #now u can play it like a dictionary
>>> ratFile['characteristics'] = ['fat', 'grey', 'thief', 'chonky']
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    ratFile['characteristics'] = ['fat', 'grey', 'thief', 'chonky']
NameError: name 'ratFile' is not defined
>>> #OOPS
>>> 
>>> shelveFile['characteristics'] = ['fat', 'grey', 'thief', 'chonky']
>>> shelveFile.close
<bound method Shelf.close of <shelve.DbfilenameShelf object at 0x110537580>>
>>> shelveFile.close()
>>> 
>>> 
>>> #lets try tor eopen it to see our new characteristics group
>>> shelveFile = shelve.open('ratFile')
>>> ratfile['characteristics']
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    ratfile['characteristics']
NameError: name 'ratfile' is not defined
>>> #oops
>>> ratFile['charactersitics']
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    ratFile['charactersitics']
NameError: name 'ratFile' is not defined
>>> #NAKO PO LETS REDO THE WHOLE THING
>>> 
>>> 
>>> import shelve
>>> 
>>> shelfFile = shelve.open('ratFile')
>>> shelfFile['characteristics'] = ['fat', 'grey', 'thief', 'chonky']
>>> shelfFile.close()
>>> 
>>> #lets reopne to check
>>> 
>>> shelfFile = shelf.open('ratFile')
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    shelfFile = shelf.open('ratFile')
NameError: name 'shelf' is not defined
>>>  shelfFile = shelve.open('ratFile')
 
SyntaxError: unexpected indent
>>> shelfFile = shelf.open('ratFile')
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    shelfFile = shelf.open('ratFile')
NameError: name 'shelf' is not defined
>>> shelfFile = shelve.open('ratFile')
>>> shelfFile['characteristics']
['fat', 'grey', 'thief', 'chonky']
>>> #NICEEEEE FINALLY
>>> 
>>> #now you must be asking what 'ratFIle' would look like in our directory
>>> #its actually a binary file so if you open it on a text editor, it comes out weird
>>> 
>>> #since shelf files are similar to dictionaries, you can get its key and value pairs
>>> 
>>> #use the list function for this
>>> #keys() and values() method for shelve module are used to get these data
>>> 
>>> 
>>> shelfFile = shelve.open('ratFile')
>>> shelfFile.keys()
KeysView(<shelve.DbfilenameShelf object at 0x110534850>)
>>> #u need to use list function
>>> list(shelfFile.keys())
['characteristics']
>>> #nICE
>>> list(shelfFile.values())
[['fat', 'grey', 'thief', 'chonky']]
>>> #NICE

>>> 
>>> 