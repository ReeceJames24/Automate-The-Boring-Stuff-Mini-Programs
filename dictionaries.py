Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #dictionaries
>>> 
>>> 
>>> 
>>> 
>>> # key-value pairs
>>> 
>>> myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
>>> myCat['size']
'fat'
>>> 'My cat has ' + myCat['color'] + ' fur'
'My cat has gray fur'
>>> 
>>> # dictionaries are unorderable
>>> 
>>> eggs = {'name': 'nooice', 'species': 'cat', 'rat: nice'}
SyntaxError: invalid syntax
>>> eggs = {'name': 'nooice', 'species': 'cat', 'rat': 'nice'}
>>> ham = {'species': 'cat', 'name': 'nooice', 'rat
       
SyntaxError: EOL while scanning string literal
>>> ham = {'species': 'cat', 'name': 'nooice', 'rat': 'nice'}
>>> eggs == ham
True
>>> # see they're considered the same
>>> 
>>> #to check if a key exists in the dictionary use in
>>> 
>>> 'name' in eggs
True
>>> 'name' not in eggs
False
>>> 
>>> # note that dictionaries are mutable meaning the actual values arent stored but rather the references
>>> 
>>> 
>>> #using methods for dictionaries

>>> list(eggs.key())
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    list(eggs.key())
AttributeError: 'dict' object has no attribute 'key'
>>> eggs = {'name': 'nooice', 'species': 'cat', 'rat': 'nice'}
>>> list(eggs.key())
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    list(eggs.key())
AttributeError: 'dict' object has no attribute 'key'
>>> list(eggs.keys())
['name', 'species', 'rat']
>>> list(eggs.values())
['nooice', 'cat', 'nice']
>>> list(eggs.items())
[('name', 'nooice'), ('species', 'cat'), ('rat', 'nice')]
>>>  # items method lists down the key value pairs as tuples
 
>>> # note that using methods on dictionaries returns list-like values
>>> # thats why u need to call the list function
>>> #this is waht happens when you dont call list
>>> 
>>> eggs.keys()
dict_keys(['name', 'species', 'rat'])
>>> # heres the list version
>>> list(eggs.keys())
['name', 'species', 'rat']
>>> 
>>> 
>>> 
>>> #using dictionaries in for looops
>>> 
>>> 
>>> for k in eggs.keys():
	print(k)

	
name
species
rat
>>> 
>>> for v in eggs.values():
	print(v)

	
nooice
cat
nice
>>> 
>>> 
>>> for k, v in eggs.items():
	print(k,v)

	
name nooice
species cat
rat nice
>>> 
>>> #dont mind this next code just checking
>>> eggs.items()
dict_items([('name', 'nooice'), ('species', 'cat'), ('rat', 'nice')])
>>> 
>>> 
>>> 

>>> 
>>> 
>>> if you use items method in forloop wtith only one variable, you get tuples instead
SyntaxError: invalid syntax
>>> #if you use items method in forloop wtith only one variable, you get tuples instead
>>> 
>>> 
>>> for i in eggs.items()
SyntaxError: invalid syntax
>>> for i in eggs.items():
	print(i)

	
('name', 'nooice')
('species', 'cat')
('rat', 'nice')
>>> 
>>> #heres what it looks like if you use multiple variables
>>> 
>>> for a, b in eggs.items():
	print (a, b)

	
name nooice
species cat
rat nice
>>> 

>>> 
>>> # get method
>>> # has 2 arguments (the key ur looking for and the falback value if the key is not retrieved)
>>> 
>>> eggs
{'name': 'nooice', 'species': 'cat', 'rat': 'nice'}
>>> egg.get('age', 0)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    egg.get('age', 0)
NameError: name 'egg' is not defined
>>> eggs.get('age',0)
0
>>> #returned 0 cause there was no age key
>>> 
>>> eggs.get('name',0)
'nooice'
>>> 
>>> 
>>> 
>>> # example of get again
>>> 
>>> picnicItems = {'apples': 5, 'eggs': 2}
>>> print('I am bringing ' + str(picnicItems.get('cheese',0)) + ' to the picnic')
I am bringing 0 to the picnic
>>> 
>>> # if you try this using the typical index rather than the get method, you'll get an error . See example below
>>> 
>>> print('I am bringing ' + str(picnicItems['cheese']) + ' to the picnic')
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    print('I am bringing ' + str(picnicItems['cheese']) + ' to the picnic')
KeyError: 'cheese'
>>> # see LOL
>>> 
>>> 
>>> 
>>> # opposite of get() method is setdefault() method
>>> 
>>> eggs
{'name': 'nooice', 'species': 'cat', 'rat': 'nice'}
>>> # to add a key value pair, you'll typically do the if not in function
>>> if 'color' not in eggs:
	eggs['color'] = 'black'

	
>>> eggs
{'name': 'nooice', 'species': 'cat', 'rat': 'nice', 'color': 'black'}
>>> # the setdefault() method allows you to do that in one line of code
>>> 
>>> eggs = {'name': 'nooice', 'species': 'cat', 'rat': 'nice'}
>>> eggs.setdefault('color', 'black')
'black'
>>> eggs
{'name': 'nooice', 'species': 'cat', 'rat': 'nice', 'color': 'black'}
>>> # nice
>>> # note that this only works if the key doesnt exist yet
>>> # meaning you cant use the setdefault() to replace a value for an existing key
>>> #see what i mean
>>> eggs.setdefault('color', 'orange')
'black'
>>> eggs
{'name': 'nooice', 'species': 'cat', 'rat': 'nice', 'color': 'black'}
>>> # no change since theres already a color key in the eggs variable