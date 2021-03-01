Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> 
>>> import os
>>> os.path.join('User','chummi','Desktop')
'User/chummi/Desktop'
>>> # this method transforms your string into a file path that follows the file path specs of whatever OS you are using (meaning the output would be diff if i were on windows0
>>> 
>>> os.sep
'/'
>>> #this is the separator for your os
>>> 
>>> 
>>> os.cwd()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    os.cwd()
AttributeError: module 'os' has no attribute 'cwd'
>>> 
>>> 
>>> #OOPS
>>> 
>>> os.getcwd()
'/Users/chummi'
>>> cd
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    cd
NameError: name 'cd' is not defined
>>> #os.getcwd() is the same as using cd in the terminal (its the pythonic version of cd cause cd is for the bash language used by your CLI or terminal)
>>> 
>>> os.getcwd()
'/Users/chummi'
>>> 
>>> #JK ITS cwd in bash NOT cd
>>> 
>>> #cd is for changing the directory
>>> 
>>> #in pythonic language, cd is os.chdir()
>>> 
>>> #example
>>> 
>>> os.chdir('/Users/chummi/Desktop')
>>> os.getcwd()
'/Users/chummi/Desktop'
>>> #see its like using cd in bash to change the directory then using cwd to check current working directory
>>> 
>>> os.chdir('/Users/chummi')
>>> os.getcwd()
'/Users/chummi'
>>> 