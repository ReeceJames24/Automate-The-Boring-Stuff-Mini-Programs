Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 

>>> #walking directory tree
>>> 
>>> #os.walk() function is used typically in loop codes for directories to get a detialed understanding of the entire directory tree
>>> 
>>> #applying loops to os.walk returns 3 values and will iterate returning 3 values all the time so oyu need ot input 3 when you set up the for loop :)
>>> 
>>> import os
>>> 
>>> for folderNames, subfolders, filenames in os.walk('/Users/chummi/Desktop/Cheken'):
	print('The folder is ' + folderNames)
	print('The subfolders in ' + folderNames + ' are:' + str(subfolders))
	print('The files in ' + folderNames + ' are:' + str(filenames))

	
The folder is /Users/chummi/Desktop/Cheken
The subfolders in /Users/chummi/Desktop/Cheken are:['Wengs', 'CHOKONWENGS']
The files in /Users/chummi/Desktop/Cheken are:['ratFile.db', 'kokster.txt', 'spam.txt']
The folder is /Users/chummi/Desktop/Cheken/Wengs
The subfolders in /Users/chummi/Desktop/Cheken/Wengs are:[]
The files in /Users/chummi/Desktop/Cheken/Wengs are:[]
The folder is /Users/chummi/Desktop/Cheken/CHOKONWENGS
The subfolders in /Users/chummi/Desktop/Cheken/CHOKONWENGS are:['Wengs']
The files in /Users/chummi/Desktop/Cheken/CHOKONWENGS are:['ratFile.db', 'kokster.txt', 'spam.txt']
The folder is /Users/chummi/Desktop/Cheken/CHOKONWENGS/Wengs
The subfolders in /Users/chummi/Desktop/Cheken/CHOKONWENGS/Wengs are:[]
The files in /Users/chummi/Desktop/Cheken/CHOKONWENGS/Wengs are:[]
>>> #NICE see how it goes through the primary directory first but also iterates within each subfolder found inside the main directory
>>> 
>>> 
>>> #you can even add more for loops within that main for loop
>>> #ex
>>> 
>>> for folderNames, subfolders, filenames in os.walk('/Users/chummi/Desktop/Cheken'):
	print('The folder is ' + folderNames)
	print('The subfolders in ' + folderNames + ' are:' + str(subfolders))
	print('The files in ' + folderNames + ' are:' + str(filenames))

	
The folder is /Users/chummi/Desktop/Cheken
The subfolders in /Users/chummi/Desktop/Cheken are:['Wengs', 'CHOKONWENGS']
The files in /Users/chummi/Desktop/Cheken are:['ratFile.db', 'kokster.txt', 'spam.txt']
The folder is /Users/chummi/Desktop/Cheken/Wengs
fThe subfolders in /Users/chummi/Desktop/Cheken/Wengs are:[]o
The files in /Users/chummi/Desktop/Cheken/Wengs are:[]r
The folder is /Users/chummi/Desktop/Cheken/CHOKONWENGS
The subfolders in /Users/chummi/Desktop/Cheken/CHOKONWENGS are:['Wengs']
The files in /Users/chummi/Desktop/Cheken/CHOKONWENGS are:['ratFile.db', 'kokster.txt', 'spam.txt']
The folder is /Users/chummi/Desktop/Cheken/CHOKONWENGS/Wengs
The subfolders in /Users/chummi/Desktop/Cheken/CHOKONWENGS/Wengs are:[]
The files in /Users/chummi/Desktop/Cheken/CHOKONWENGS/Wengs are:[]
>>> 
>>> 
>>> import os
>>> import shutil
>>> 
>>> for folderNames, subfolders, filenames in os.walk('/Users/chummi/Desktop/Cheken'):
	print('The folder is ' + folderNames)
	print('The subfolders in ' + folderNames + ' are:' + str(subfolders))
	print('The files in ' + folderNames + ' are:' + str(filenames))
	for subfolder in subfolders:
		if 'fish' in subfolder:
			os.rmdir(subfolder) #this for loop wil remove all subfolders w fish name
	for filename in filenames:
		if filename.endswith('.txt'):
			shutil.copy(os.join(folderName, file), os.join(folderName, file + '.backup')) #this loops looks for the txt files and creates copies for them in the same folder and naming them the same name + backup

			
The folder is /Users/chummi/Desktop/Cheken
The subfolders in /Users/chummi/Desktop/Cheken are:['Wengs', 'CHOKONWENGS']
The files in /Users/chummi/Desktop/Cheken are:['ratFile.db', 'kokster.txt', 'spam.txt']
Traceback (most recent call last):
  File "<pyshell#35>", line 10, in <module>
    shutil.copy(os.join(folderName, file), os.join(folderName, file + '.backup')) #this loops looks for the txt files and creates copies for them in the same folder and naming them the same name + backup
AttributeError: module 'os' has no attribute 'join'
>>> #OOPS lets do that again
>>> 
>>> for folderNames, subfolders, filenames in os.walk('/Users/chummi/Desktop/Cheken'):
	print('The folder is ' + folderNames)
	print('The subfolders in ' + folderNames + ' are:' + str(subfolders))
	print('The files in ' + folderNames + ' are:' + str(filenames))
	for subfolder in subfolders:
		if 'fish' in subfolder:
			os.rmdir(subfolder) #this for loop wil remove all subfolders w fish name
	for filename in filenames:
		if filename.endswith('.txt'):
			shutil.copy(join(folderName, file), join(folderName, file + '.backup')) #this loops looks for the txt files and creates copies for them in the same folder and naming them the same name + backup
			
SyntaxError: invalid syntax
>>> 
>>> oops it should be os.path.join
SyntaxError: invalid syntax
oops it should be os.path.join
>>> 
>>> #lets redo
>>> 
>>> 
>>> for folderNames, subfolders, filenames in os.walk('/Users/chummi/Desktop/Cheken'):
	print('The folder is ' + folderNames)
	print('The subfolders in ' + folderNames + ' are:' + str(subfolders))
	print('The files in ' + folderNames + ' are:' + str(filenames))
	for subfolder in subfolders:
		if 'fish' in subfolder:
			os.rmdir(subfolder) #this for loop wil remove all subfolders w fish name
	for filename in filenames:
		if filename.endswith('.txt'):
			shutil.copy(os.path.join(folderName, file), os.path.join(folderName, file + '.backup')) #this loops looks for the txt files and creates copies for them in the same folder and naming them the same name + backup
			
SyntaxError: invalid syntax
>>> for folderNames, subfolders, filenames in os.walk('/Users/chummi/Desktop/Cheken'):
	print('The folder is ' + folderNames)
	print('The subfolders in ' + folderNames + ' are:' + str(subfolders))
	print('The files in ' + folderNames + ' are:' + str(filenames))
	for subfolder in subfolders:
		if 'fish' in subfolder:
			os.rmdir(subfolder) #this for loop wil remove all subfolders w fish name
	for filename in filenames:
		if filename.endswith('.txt'):
			shutil.copy(os.path.join(folderName, file), os.path.join(folderName, file + '.backup')) #this loops looks for the txt files and creates copies for them in the same folder and naming them the same name + backup
>>> 