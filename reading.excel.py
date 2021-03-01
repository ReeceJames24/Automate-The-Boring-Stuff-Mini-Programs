Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Reading Excel Spreadsheets
>>> 
>>> import openpyxl
>>> #lets change dir first to where we downloaded our exel file
>>> 
>>> import os
>>> os.getcwd()
'/Users/chummi/Desktop'
>>> os.chdir('/Users/chummi/Downloads')
>>> os.getcwd()
'/Users/chummi/Downloads'
>>> #nice
>>> 
>>> workbook = openpyxl.load_workbook('example.xlsx')
>>> #lets just make sure its a workbook
>>> type(workbook)
<class 'openpyxl.workbook.workbook.Workbook'>
>>> #nice
>>> 
>>> #lets now get the sheet names
>>> workbook.get_sheet_names()

Warning (from warnings module):
  File "<pyshell#17>", line 1
DeprecationWarning: Call to deprecated function get_sheet_names (Use wb.sheetnames).
['Sheet1', 'Sheet2', 'Sheet3']
>>> #okay nice lets save the first sheet as a varibale
>>> 
>>> sheet1 = workbook.get_sheet_by_name('Sheet1')

Warning (from warnings module):
  File "<pyshell#20>", line 1
DeprecationWarning: Call to deprecated function get_sheet_by_name (Use wb[sheetname]).
>>> #OH i think these are outdated code
>>> 
>>> 
>>> #lets retry it with the newer version to see if we still get any errors
>>> 
>>> workbook.sheetnames
['Sheet1', 'Sheet2', 'Sheet3']
>>> #OH NICE
>>> 
>>> sheet1 = workbook['Sheet1']
>>> sheet1
<Worksheet "Sheet1">
>>> #NICEEE MUCH EASIER THANKS STACKOVERFLOW
>>> 
>>> #now lets get the value of a cell
>>> 
>>> #lets say u want cell A1
>>> 
>>> sheet1['A1']
<Cell 'Sheet1'.A1>
>>> #this doesnt actually return the contents of the cell so u have to assign it first to a variable then use .value
>>> 
>>> cellA1 = sheet1['A1']
>>> cellA1.value
datetime.datetime(2015, 4, 5, 13, 34, 2)
>>> #ntoe that it returns that sicne its formated as a date in excel, lets convert it to a string to udnerstand it
>>> str(cellA1.value)
'2015-04-05 13:34:02'
>>> #there we go!
>>> 
>>> #lets now check the values of other cells
>>> 
>>> sheet1['B1'].value
'Apples'
>>> sheet1['C1'].value
73
>>> #if you dont want to use name of cell, you can do this
>>> 
>>> sheet1.cell(row=1, column=2)
<Cell 'Sheet1'.B1>
>>> #this the exact same as sheet1['B1']
>>> sheet1['B1']
<Cell 'Sheet1'.B1>
>>> # see!
>>> 
>>> #this is useful for when you want to do for loops
>>> 
>>> for i in range(1, 8):
	print(i, sheet1.cell(row=1=i, column=2).value)
	
SyntaxError: invalid syntax
>>> #OOPS
>>> for i in range (1, 8):
	print(i, sheet1.cell(row=i, column = 2).value)

	
1 Apples
2 Cherries
3 Pears
4 Oranges
5 Apples
6 Bananas
7 Strawberries
>>> # NICE see u didnt have to manaull place b1, b2, b3,b4 etc
>>> 
>>> 