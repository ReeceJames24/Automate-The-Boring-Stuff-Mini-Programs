Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #mutable and immutable values
>>> 
>>> #strings are immutable while lists are mutable
>>> #since lsits are immutable, you might encounter reference issues. See example below
>>> 
>>> 
>>> 
>>> spam = ['1','2','3','4','5']
>>> cheese = spam
>>> cheese[1] = 'eggs'
>>> cheese
['1', 'eggs', '3', '4', '5']
>>> spam
['1', 'eggs', '3', '4', '5']
>>> # you can see that the spam variable was also changed with the cheese index
>>> 
>>> #the reason why is because assigning lists to a variable don't actually place the list inside them. Python matches a reference id to them
>>> # since both spam and cheese refer to the exact same list, python gives them the same reference id hence any changes in cheese variable also will result to the exact same change in the spam variable
>>> 
>>> 
>>> # immutable values dont encounter this issue since they can't be modified "in place". They can only be replaced by new values
>>> 
>>> 
>>> #bonus notes:
>>> # using line slash tells python that you're still on the same code even if its on the next line already. See example below
>>> 
>>> 
>>> print('bacon and ' + 'eggs')
bacon and eggs
>>> print ('bacon and ' + \
	       'eggs')
bacon and eggs
>>> #see they;re the same
>>> 
>>> 
>>> # how to change then the cheese variable from the example above without affecting the spam variable? you need to create a new reference id for that list (basically creating a complete copy of that list) using an the copy module
>>> import copy
>>> 
>>> spam = ['1','2','3','4','5']
>>> cheese = copy.deepcopy(spam)
>>> cheese[1] = 'hot'
>>> cheese
['1', 'hot', '3', '4', '5']
>>> spam
['1', '2', '3', '4', '5']
>>> # NICE
>>> 
>>> 
>>> #bonus note: when you are passing a list argument to a function, you are actually passing a list reference (see def.mutable)
>>> 