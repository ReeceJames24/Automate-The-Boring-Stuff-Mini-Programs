Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> ## DELETING FILES
>>> 
>>> 
>>> #you can delete single files through the os module's unlink method
>>> 
>>> #ex: os.unlink('spam.txt')
>>> # note that since i placed a relative file path, it will look for that file in the cwd so might be best to hit up a os.getcwd() first to check ur cwd
>>> 
>>> 
>>> #os.rmdir() is used to delete folders!
>>> import os
>>> os.rmdir('/Users/chummi/Desktop/Cheken')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    os.rmdir('/Users/chummi/Desktop/Cheken')
OSError: [Errno 66] Directory not empty: '/Users/chummi/Desktop/Cheken'
>>> #NOTE THAT THIS ONLY WORKS ON EMPTY FOLDERS!!!
>>> 
>>> #if you want to delete folders w content, you need to use rmtee method of shutil module. This is like the delete version of the copytree module
>>> 
>>> import shutil
>>> shutil.rmtree('/Users/chummi/Desktop/Cheken/Cheken_backup')
>>> #i is now gone.
>>> #note that you ened to be careful witht his since it permanently deletes the folder and all its contents. It doesnt just send it to the bin
>>> 
>>> #to be safe, you can do a DRY RUN before running any programs with delete code scripts. This basically just means you put a # before the deleting script followedby a print funcrion of the filename to see if you would have deleted an important file if the deleting script wasnt just a comment. See example below
>>> 
>>> import os
>>> # its going to look like this
>>> # for filename in os.listdir():
>>> #     if filename.endswith('.rxt'):
>>> #           #os.unlink(filename)
>>> #            print(filename)
>>> 
>>> 
>>> 
>>> # seee now when you run that program, you'll get a printout of the filename that you would have deleted should you have ran that program
>>> 
>>> 
>>> #to be safe, you should jsut use the send2trash module with its send2trash method
>>> 
>>> 
>>> #u need to pip install first but this is how its gonna look like
>>> #   import send2trash
>>> #   send2trash.send2trash('your file path')
>>> 
>>> # this sends it only to the bin and does not permanently delete it
>>> 
>>> 
>>> 