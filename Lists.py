Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> spam = 'hello'
>>> spam
'hello'
>>> spam = ['eggs', 'nice']
>>> spam
['eggs', 'nice']
>>> spam[1]
'nice'
>>> spam[0]
'eggs'
>>> spam = ['eggs', 'nice', 'rats', 'bacon']
>>> spam
['eggs', 'nice', 'rats', 'bacon']
>>> spam[1:3]
['nice', 'rats']
>>> spam[0]
'eggs'
>>> spam[0] = 'crock pan'
>>> spam
['crock pan', 'nice', 'rats', 'bacon']
>>> spam[0:]
['crock pan', 'nice', 'rats', 'bacon']
>>> spam[:2]
['crock pan', 'nice']
>>> del spam[1]
>>> spam
['crock pan', 'rats', 'bacon']
>>> 
>>> 
>>> len('hello')
5
>>> len([1,2,3,4])
4
>>> [1,2,3] + [4,5,6]
[1, 2, 3, 4, 5, 6]
>>> [1,2,3] * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> list('hello')
['h', 'e', 'l', 'l', 'o']
>>> 
>>> 
>>> # IN AND NOT IN OPERATORS
>>> 
>>> 'nice' in ['eggs', 'nice', 'rats', 'bacon']
True
>>> 'nice' not in ['eggs', 'nice', 'rats', 'bacon']
False
>>> 69 in ['eggs', 'nice', 'rats', 'bacon']
False
>>> spam[0] = 'crock pan'
>>> spam[-1]
'bacon'
>>> spam
['crock pan', 'rats', 'bacon']
>>> spam[-2]
'rats'
>>> 