Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #the shutil module allows you to move, copy, rename, and delete files through python
>>> 
>>> 
>>> import shutil
>>> #shutil's copy method allows you to copy specific files into different folders (also allows you to rename the copied verisons)
>>> 
>>> shutil.copy('/Users/chummi/Desktop/Cheken/spam.txt', '/Users/chummi/Desktop')
'/Users/chummi/Desktop/spam.txt'
>>> #NICE IT MADE A COPY
>>> #you can also specify a new name for the copy
>>> shutil.copy('/Users/chummi/Desktop/Cheken/spam.txt', '/Users/chummi/Desktop/spum.txt')
'/Users/chummi/Desktop/spum.txt'
>>> ##NICE
>>> 
>>> #to copy an entire folder, use copytree method
>>> 
>>> shutil.copytree('/Users/chummi/Desktop/Cheken', '/Users/chummi/Desktop')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    shutil.copytree('/Users/chummi/Desktop/Cheken', '/Users/chummi/Desktop')
  File "/opt/anaconda3/lib/python3.8/shutil.py", line 554, in copytree
    return _copytree(entries=entries, src=src, dst=dst, symlinks=symlinks,
  File "/opt/anaconda3/lib/python3.8/shutil.py", line 455, in _copytree
    os.makedirs(dst, exist_ok=dirs_exist_ok)
  File "/opt/anaconda3/lib/python3.8/os.py", line 223, in makedirs
    mkdir(name, mode)
FileExistsError: [Errno 17] File exists: '/Users/chummi/Desktop'
>>> #oops doesnt work cos its alrready there KEKEKKE
>>> #let us redo that w a diff name
>>> 
>>> 
>>> shutil.copytree('/Users/chummi/Desktop/Cheken', '/Users/chummi/Desktop/Cheken_backup')
'/Users/chummi/Desktop/Cheken_backup'
>>> #NICE IT WORKED
>>> 
>>> 
>>> #now to move files we use the move method
>>> 
>>> shutil.move('/Users/chummi/Desktop/Cheken_backup', '/Users/chummi/Desktop/Cheken')
'/Users/chummi/Desktop/Cheken/Cheken_backup'
>>> ## NICE IT WORKED
>>> 
>>> #to rename, there no rename method but you can just do the move method but place it in the exact same destination w a new name :)