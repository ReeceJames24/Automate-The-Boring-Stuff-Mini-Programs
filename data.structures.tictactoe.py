Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 

>>> 
>>> # data structures
>>> # a list of dictionaries is called a data structure
>>> 
>>> #example of a data structure of your cats

>>> cat = {'name': 'wonka', 'age': '9', 'color': 'black')
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
>>> cat = {'name': 'wonka', 'age': '9', 'color': 'black'}
>>> allCats=[]
>>> allCats.append(cat)
>>> allCats.append({'name': 'chonky', 'age': '69', 'color': 'blue'})
>>> allCats.append({'name': 'randy', 'age': '2', 'color': 'red'})
>>> allCats
[{'name': 'wonka', 'age': '9', 'color': 'black'}, {'name': 'chonky', 'age': '69', 'color': 'blue'}, {'name': 'randy', 'age': '2', 'color': 'red'}]
>>> #nice

>>> 

>>> #creating a tic-tac-toe boar dusing data structures
>>> theBoard = {'top-L': '', 'top-M': '', 'top-R': '', 'mid-L': '', 'mid-M': '', 'mid-R': '', 'low-L': '', 'low-M': '', 'low-R': ''}
>>> theBoard
{'top-L': '', 'top-M': '', 'top-R': '', 'mid-L': '', 'mid-M': '', 'mid-R': '', 'low-L': '', 'low-M': '', 'low-R': ''}
>>> import pprint
>>> pprint.pprint(theBoard)
{'low-L': '',
 'low-M': '',
 'low-R': '',
 'mid-L': '',
 'mid-M': '',
 'mid-R': '',
 'top-L': '',
 'top-M': '',
 'top-R': ''}
>>> #nice lets try adding Xs and Os
>>> theBoard['top-L'] = 'O'
>>> theBoard['top-M'] = 'O'
>>> theBoard['top-R'] = 'O'
>>> theBoard['mid-L'] = 'X'
>>> theBoard['low-R'] = 'X'
>>> 

>>> 
>>> pprint.pprint(theBoard)
{'low-L': '',
 'low-M': '',
 'low-R': 'X',
 'mid-L': 'X',
 'mid-M': '',
 'mid-R': '',
 'top-L': 'O',
 'top-M': 'O',
 'top-R': 'O'}
>>> # but it doesnt look like a board?
>>> #lets make a function to do that

>>> 
>>> def printBoard(board):
	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
	print('-----')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

	
>>> printBoard(theBoard)
O|O|O
-----
X||
||X
>>> # oops lets put spaces on the blanks in the data structure
>>> 
>>> theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
>>> pprint.pprint(theBoard)
{'low-L': ' ',
 'low-M': ' ',
 'low-R': ' ',
 'mid-L': ' ',
 'mid-M': ' ',
 'mid-R': ' ',
 'top-L': ' ',
 'top-M': ' ',
 'top-R': ' '}
>>> #nice looking good lets call the function we just made again
>>> 
>>> printBoard(theBoard)
 | | 
-----
 | | 
 | | 
>>> #oops sorry i forgot to put the lines under the middle row
>>> 

>>> def printBoard(board):
	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
	print('-----')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
	print('-----')
	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

	
>>> 
>>> # lets check again

>>> printBoard(theBoard)
 | | 
-----
 | | 
-----
 | | 
>>> # nice
>>> 
>>> # lets try adding inputs
>>> 
>>> theBoard['top-L'] = 'O'
>>> theBoard['top-M'] = 'O'
>>> theBoard['top-R'] = 'O'
>>> theBoard['mid-L'] = 'X'
>>> theBoard['top-L'] = 'O'
>>> theBoard['low-R'] = 'X'
>>> 

>>> theBoard
{'top-L': 'O', 'top-M': 'O', 'top-R': 'O', 'mid-L': 'X', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': 'X'}
>>> pprint.pprint(theBoard)
{'low-L': ' ',
 'low-M': ' ',
 'low-R': 'X',
 'mid-L': 'X',
 'mid-M': ' ',
 'mid-R': ' ',
 'top-L': 'O',
 'top-M': 'O',
 'top-R': 'O'}
>>> 

>>> printBoard(theBoard)
O|O|O
-----
X| | 
-----
 | |X
>>> # NICE