Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> #creating and editing excel files
>>> 
>>> 
>>> import openpyxl

>>> #instead of using variable = openpyxl.load_Workbook('filename'), we use variable = openpyxl.Workbook() to create a blank workbook
>>> 
>>> wb = openpyxl.Workbook()
>>> #this creates a blank workbook with 1 sheet called 'Sheet'
>>> wb.sheetnames
['Sheet']
>>> #see
>>> 
>>> sheet = wb.get_sheet_by_name('Sheet')

Warning (from warnings module):
  File "<pyshell#12>", line 1
DeprecationWarning: Call to deprecated function get_sheet_by_name (Use wb[sheetname]).
>>> #OOPS lets make it easier
>>> 
>>> sheet = wb['Sheet']
>>> sheet['A1'] == None
False
>>> #wot it should be empty i have no clue why it aint
>>> 
>>> str(sheet['A1'].value)
'None'
>>> #wth theres none naman thats weird LOL
>>> 
>>> #if we wanna add content to the cells, we assign like variable
>>> 
>>> sheet['A1'] = 42
>>> sheet['A2'] = 'Hello'
>>> 
>>> #lets save this now to PyPrac
>>> 
>>> import os
>>> os.getcwd()
'/Users/chummi/Desktop'
>>> os.chdir('/Users/chummi/Desktop/PyPrac')
>>> os.getcwd()
'/Users/chummi/Desktop/PyPrac'
>>> wb.save('examplefile.xlsx')
>>> #nice i checked it the file is in pyprac and the values we added r there nice
>>> 
>>> #now lets crate a new sheet for it

>>> 
>>> wb.create_sheet()
<Worksheet "Sheet1">
>>> wb.sheetnames
['Sheet', 'Sheet1']
>>> #if we want to change the name
>>> 
>>> #lets assign it to a variable first to make it easier
>>> newsheet = wb.create_sheet()
>>> newsheet.title
'Sheet2'
>>> #les change that
>>> 
>>> newsheet.title('My newest sheet')
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    newsheet.title('My newest sheet')
TypeError: 'str' object is not callable
>>> #OOOPS
>>> 
>>> newsheet.title = 'My newest sheet'
>>> wb.sheetnames
['Sheet', 'Sheet1', 'My newest sheet']
>>> #there we go
>>> 
>>> 
>>> wb['Sheet'].title = 'Sheet 1'
>>> wb['Sheet1'].title = 'Sheet 2'
>>> wb.sheetnames
['Sheet 1', 'Sheet 2', 'My newest sheet']
>>> #NICE
>>> 
>>> #oops it didnt reflect cos i didnt save it
>>> 
>>> wb.save('examplefileV2.xlsx')
>>> #nice i saved it under a new file and yea it reflected
>>> 
>>> #now what if we want to add a new sheet somehwere but not just to add it on top of the existing sheets:?
>>> 
>>> #we use index with the create_sheet
>>> 
>>> wb.create_sheet(index=0, title = 'My other sheet')
<Worksheet "My other sheet">
>>> wb.save('examplefileV2.slsx')
>>> #OOPS
>>> 
>>> wb.save('examplefileV2.xlsx')
>>> #nice it worked!!
>>> 
>>> #note that .title is called a title member variable
>>> #.save is a method