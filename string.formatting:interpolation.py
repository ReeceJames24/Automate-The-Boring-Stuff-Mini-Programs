Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # string formatting
>>> 
>>> 'hello' + 'world'
'helloworld'
>>> 
>>> 
>>> name = 'alice'
>>> place = 'main street'
>>> time = '6 pm'
>>> food = 'turnips'
>>> 'Hello' + name + ', you are cordially invited to a party at ' + place + ' at ' + time + '. Please bring ' + food + '.'
'Helloalice, you are cordially invited to a party at main street at 6 pm. Please bring turnips.'
>>> #this string concatenation is kinda hassle to do when you have a lot of strings to concatenate
>>> 
>>> # we do string formatting (aka string interpolation) to do this easier
>>> 
>>> # see example below
>>> 
>>> 'Hello %s, you are cordially invited to a party at %s at %s. Please bring %s.' % (name, place, time, food)
'Hello alice, you are cordially invited to a party at main street at 6 pm. Please bring turnips.'
>>> # see!!! sick huh
>>> 
>>> # note that the %s are called conversion specifiers
>>> # place % after the string  followed by comma delimited values of the variable you want in order of the placement of your conversion specifiers within parentheses.
>>> 
>>> 
>>> 
>>> 