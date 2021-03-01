Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> 
>>> # using for loops with ranges, lists, and len
>>> range(4)
range(0, 4)
>>> list(range(4))
[0, 1, 2, 3]
>>> list(range(0,100,2))
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
>>> spam = list(range(4))
>>> spam
[0, 1, 2, 3]
>>> supplies = ['egg', 'bacon', 'crab', 'socks']
>>> for i in range(len(supplies))
SyntaxError: invalid syntax
>>> for i in range(len(supplies)):
	print('Index #' + str(i) + ' in supplies is: ' + supplies[i])

	
Index #0 in supplies is: egg
Index #1 in supplies is: bacon

Index #2 in supplies is: crab
Index #3 in supplies is: socks
>>> 
>>> 