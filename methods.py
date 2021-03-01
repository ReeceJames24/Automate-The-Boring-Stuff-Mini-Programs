Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 

>>> 
>>> spam = ['cat', 'dog', 'rat']
>>> spam += 'eggs'
>>> spam
['cat', 'dog', 'rat', 'e', 'g', 'g', 's']
>>> spam += ['eggs']
>>> spam
['cat', 'dog', 'rat', 'e', 'g', 'g', 's', 'eggs']
>>> spam.append('nice')
>>> spam
['cat', 'dog', 'rat', 'e', 'g', 'g', 's', 'eggs', 'nice']
>>> 
>>> 
>>> #methods
>>> 
>>> spam.insert(1, 'chonky')
>>> spam
['cat', 'chonky', 'dog', 'rat', 'e', 'g', 'g', 's', 'eggs', 'nice']
>>> # sets chonky string as the new number 1 of the list
>>> 
>>> A = 'nice'
>>> A.append('eggs')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    A.append('eggs')
AttributeError: 'str' object has no attribute 'append'
>>> #doesnt work since append, remove, and insert are list methods not string methods
>>> 
>>> spam = ['cat', 'bat', 'rat']
>>> spam.remove('cat')
>>> spam
['bat', 'rat']
>>> #remove lets yous specify the value while the del function only lets you choose the index see below
>>> spam = ['eggs', 'nice', 'rat']
>>> del spam[1]
>>> spam
['eggs', 'rat']
>>> spam.remove('eggs')
>>> spam
['rat']
>>> #note that remove method only removes the first found instance see ex below
>>> spam = ['cat', 'rat', 'dog', 'rat', 'rat']
>>> spam.remove('rat')
>>> spam
['cat', 'dog', 'rat', 'rat']
>>> 
>>> 
>>> # sort method
>>> 
>>> spam = [1,3,2,3.14,5,-8,69]
>>> spam.sort()
>>> spam
[-8, 1, 2, 3, 3.14, 5, 69]

>>> 
>>> # sorth method can also be used  on strings
>>> 
>>> spam = ['cat', 'ant', 'boy', 'elephant','xerxes', 'nice']
>>> spam.sort()
>>> spam
['ant', 'boy', 'cat', 'elephant', 'nice', 'xerxes']
>>> 
>>> 
>>> 
>>> # you can also use keyword arguments with these methods see example below
>>> 
>>> spam.sort(reverse=True)
>>> spam
['xerxes', 'nice', 'elephant', 'cat', 'boy', 'ant']
>>> # this sorts the list values in reverse alphabetical order
>>> 
>>> # note that oyu can;t use sort method for a list that has a combination of both strings and integers/floats (unorderable error)
>>> 
>>> #fun fact: sort doesnt sort your strings in alphabetical order
>>> # it uses what you call ASCIIbetical order which means all uppercase come before any lowercase letters regardless of alphabetical order
>>> 
>>> e
>>> #example
>>> spam = ['a', 'B', 'c', 'D']
>>> spam.sort()
>>> spam
['B', 'D', 'a', 'c']
>>> # if you want alphabetical order, you need to use a keyword argument
>>> 
>>> spam.sort(key=str.lower)
>>> spam
['a', 'B', 'c', 'D']
>>> 
>>> 
>>> recap
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    recap
NameError: name 'recap' is not defined
>>> #recap
>>> 
>>> #methods are functions that are "called on" values
>>> # these lists operate on the "list in place' rather than returning a new list value which is why the syntax is not like spam = spam.append(cajsndsk)