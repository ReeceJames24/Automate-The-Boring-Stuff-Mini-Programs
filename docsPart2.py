Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #documents part 2 lol
>>> 
>>> import docx
>>> d = docx.Document('/Users/chummi/Desktop/demo.docx')
>>> d.paragraph[0]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    d.paragraph[0]
AttributeError: 'Document' object has no attribute 'paragraph'
>>> #oops
>>> d.paragraphs[0]
<docx.text.paragraph.Paragraph object at 0x10a09e100>
>>> d.paragraphs[0].text
'DEMO chickens like to eat food in the house of Joe.'
>>> #nice
>>> P = d.paragraphs[0]
>>> P.runs
[<docx.text.run.Run object at 0x10a09e0a0>, <docx.text.run.Run object at 0x10a09e220>, <docx.text.run.Run object at 0x10a09e2b0>, <docx.text.run.Run object at 0x10a09e460>, <docx.text.run.Run object at 0x10a09e340>, <docx.text.run.Run object at 0x10a09e520>]
>>> P.runs[0].text
'DEMO'
>>> P.runs[1].text
' chickens like to eat '
>>> P.runs[2].text
'food in'
>>> P.runs[3].text
' '
>>> #These are all the runs in that paragraph
>>> #we can even check the type
>>> 
>>> P.runs[1].text.bold
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    P.runs[1].text.bold
AttributeError: 'str' object has no attribute 'bold'
>>> #oops
>>> P.runs[1].bold
>>> P.runs[1].bold == None
True
>>> P.runs[1].italic
>>> P.runs[2].italic
True
>>> #oh so now we know 'food in' is in italics
>>> 
>>> #we can change the runs and even the text for those runs using python
>>> 
>>> P.runs[1].text
' chickens like to eat '
>>> P.runs[1].italic = True
>>> P.runs[1].text = ' Rats like to munch on '
>>> P.save('/Users/chummi/Desktop/demo.docx')
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    P.save('/Users/chummi/Desktop/demo.docx')
AttributeError: 'Paragraph' object has no attribute 'save'
>>> #OOPS i tried saving the paragraph variable lol sorry
>>> d.save('/Users/chummi/Desktop/demo.docx')
>>> #NICE I CHECKED IT IT CHANGED IT :+}
>>> 
>>> #note that you can also set the styles yourelf (styles meaning title, heading 1 , heading 2, etc.)
>>> 
>>> #lets say we want paragraph 0 to become title style also
>>> 
>>> P = d.paragraphs[0]
>>> P.text
'DEMO Rats like to munch on food in the house of Joe.'
>>> #ok lets make this title style
>>> 
>>> P.style = 'Title'
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    P.style = 'Title'
  File "/opt/anaconda3/lib/python3.8/site-packages/docx/text/paragraph.py", line 110, in style
    style_id = self.part.get_style_id(
  File "/opt/anaconda3/lib/python3.8/site-packages/docx/parts/document.py", line 78, in get_style_id
    return self.styles.get_style_id(style_or_name, style_type)
  File "/opt/anaconda3/lib/python3.8/site-packages/docx/styles/styles.py", line 109, in get_style_id
    return self._get_style_id_from_name(style_or_name, style_type)
  File "/opt/anaconda3/lib/python3.8/site-packages/docx/styles/styles.py", line 139, in _get_style_id_from_name
    return self._get_style_id_from_style(self[style_name], style_type)
  File "/opt/anaconda3/lib/python3.8/site-packages/docx/styles/styles.py", line 53, in __getitem__
    raise KeyError("no style with name '%s'" % key)
KeyError: "no style with name 'Title'"
>>> #oops thats weird
>>> 
>>> #lets try another style
>>> 
>>> P.style = 'Heading 1'
>>> #OH I GET IT I MMEADE A MISTAKE WITH TITEL
>>> 
>>> P.style = 'Title'
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    P.style = 'Title'
  File "/opt/anaconda3/lib/python3.8/site-packages/docx/text/paragraph.py", line 110, in style
    style_id = self.part.get_style_id(
  File "/opt/anaconda3/lib/python3.8/site-packages/docx/parts/document.py", line 78, in get_style_id
    return self.styles.get_style_id(style_or_name, style_type)
  File "/opt/anaconda3/lib/python3.8/site-packages/docx/styles/styles.py", line 109, in get_style_id
    return self._get_style_id_from_name(style_or_name, style_type)
  File "/opt/anaconda3/lib/python3.8/site-packages/docx/styles/styles.py", line 139, in _get_style_id_from_name
    return self._get_style_id_from_style(self[style_name], style_type)
  File "/opt/anaconda3/lib/python3.8/site-packages/docx/styles/styles.py", line 53, in __getitem__
    raise KeyError("no style with name '%s'" % key)
KeyError: "no style with name 'Title'"
>>> #JK its weird
>>> 
>>> #lets go back to heading
>>> 
>>> P.style = 'Heading 1'
>>> d.save
<bound method Document.save of <docx.document.Document object at 0x10a093dc0>>
>>> #oops
>>> d.save('/Users/chummi/Desktop/demo.docx')
>>> #NICE IT WOKRED
>>> 
>>> #lets create a new doc file
>>> #use variable = docx.Document() with no argument to save a new docx file ONLY WITHIN THE PYTHON SHELL
>>> #meaning you still have to save it in a specific directory if you want it in your drive later on
>>> 
>>> dok = docx.Document()
>>> dok.add_paragraph('Whats up dude ur not ugly always remember that')
<docx.text.paragraph.Paragraph object at 0x10a1213d0>
>>> dok.paragraphs[1].text
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    dok.paragraphs[1].text
IndexError: list index out of range
>>> #oops
>>> dok.paragraphs[0].text
'Whats up dude ur not ugly always remember that'
>>> #nice
>>> dok.add_paragraph('Just remmeber ur not at ur final form yet just be patient')
<docx.text.paragraph.Paragraph object at 0x106a51820>
>>> dok.paragraphs[1].text
'Just remmeber ur not at ur final form yet just be patient'
>>> #nice

>>> #lets save it to the drive
>>> dok.save('/Users/chummi/Desktop/newdemo.docx')
>>> #lets make some edits
>>> 
>>> dok.paragraphs[0].style = 'Heading 1'
>>> dok.paragraphs[1].runs.italic = True
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    dok.paragraphs[1].runs.italic = True
AttributeError: 'list' object has no attribute 'italic'
>>> #oops
>>> dok.paragraphs[1].runs[0].italic = True
>>> #nice remmeber that i had to put runs[0] since theres only 1 run in paragraph 1
>>> 
>>> dok.save('/Users/chummi/Desktop/newdemo.docx')
>>> #NICE It WORKED
>>> 
>>> #lets add runs.
>>> #paragraph objects also have an add_run method
>>> 
>>> dok.paragraphs[1].add_run('This is a new run LOL.')
<docx.text.run.Run object at 0x10a121a60>
>>> r = dok.paragraphs[1].add_run('New run again but bold.')
>>> r.dok.pargraphs[1].runs[2].bold = True
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    r.dok.pargraphs[1].runs[2].bold = True
AttributeError: 'Run' object has no attribute 'dok'
>>> #oops
>>> dok.paragraphs[1].runs[2].bold = True
>>> dok.save('/Users/chummi/Desktop/newdemo.docx')
>>> # NICE IT WORKED
>>> 

>>> #MODIFYING EXISTING DOCUMENT
>>> #you're goin to open the existing word document and creating a new docx.Document and copying all the content form the existing docu to the newly created docand making the changes while youre copying it over
>>> 
>>> #lets create a small program that will do that for us
>>> 
========== RESTART: /Users/chummi/Desktop/PyPrac/Doc_Text_Extractor.py =========
Traceback (most recent call last):
  File "/Users/chummi/Desktop/PyPrac/Doc_Text_Extractor.py", line 5, in <module>
    Print('Input Root Path of docx file')
NameError: name 'Print' is not defined
>>> 
========== RESTART: /Users/chummi/Desktop/PyPrac/Doc_Text_Extractor.py =========
/Users/chummi/Desktop/newdemo.docx
Traceback (most recent call last):
  File "/Users/chummi/Desktop/PyPrac/Doc_Text_Extractor.py", line 15, in <module>
    Print(DocCopier(filename))
NameError: name 'Print' is not defined
>>> 
========== RESTART: /Users/chummi/Desktop/PyPrac/Doc_Text_Extractor.py =========
Input Root Path of docx file
/Users/chummi/Desktop/newdemo.docx
Whats up dude ur not ugly always remember that
Just remmeber ur not at ur final form yet just be patientThis is a new run LOL.New run again but bold.
>>> #NICE
>>> 
===== RESTART: /Users/chummi/Desktop/PyPrac/TEST.numberIdentifier.regex.py =====
Input Statement
my number is 0916-118-2689
Phone numbers found: ['0916-118-2689']
Input Statement
my number is 0917-999-1154 and 0999-999-1110
Phone numbers found: ['0917-999-1154', '0999-999-1110']
Input Statement

========== RESTART: /Users/chummi/Desktop/PyPrac/Doc_Text_Extractor.py =========
Input Root Path of docx file
/Users/chummi/Desktop/demo.docx
DEMO Rats like to munch on food in the house of Joe.

Random text lolololol

Heading , level 1
	Chicken run




Ddskdksncmasdwmlaslxs,xl,sxa
Dssdsadasd

Input Root Path of docx file
/Users/chummi/Desktop/newdemo.docx
Whats up dude ur not ugly always remember that
Just remmeber ur not at ur final form yet just be patientThis is a new run LOL.New run again but bold.
Input Root Path of docx file

========== RESTART: /Users/chummi/Desktop/PyPrac/Doc_Text_Extractor.py =========
Input Root Path of docx file
/Users/chummi/Desktop/newdemo.docx
Whats up dude ur not ugly always remember that
Just remmeber ur not at ur final form yet just be patientThis is a new run LOL.New run again but bold.
Copying full text to clipboard....
Full text has been copied to clipboard successfully
Input Root Path of docx file
Whats up dude ur not ugly always remember that
Just remmeber ur not at ur final form yet just be patientThis is a new run LOL.New run again but bold.
Traceback (most recent call last):
  File "/Users/chummi/Desktop/PyPrac/Doc_Text_Extractor.py", line 21, in <module>
    print(DocCopier(filename))
  File "/Users/chummi/Desktop/PyPrac/Doc_Text_Extractor.py", line 14, in DocCopier
    doc = docx.Document(filename)
  File "/opt/anaconda3/lib/python3.8/site-packages/docx/api.py", line 25, in Document
    document_part = Package.open(docx).main_document_part
  File "/opt/anaconda3/lib/python3.8/site-packages/docx/opc/package.py", line 128, in open
    pkg_reader = PackageReader.from_file(pkg_file)
  File "/opt/anaconda3/lib/python3.8/site-packages/docx/opc/pkgreader.py", line 32, in from_file
    phys_reader = PhysPkgReader(pkg_file)
  File "/opt/anaconda3/lib/python3.8/site-packages/docx/opc/phys_pkg.py", line 30, in __new__
    raise PackageNotFoundError(
docx.opc.exceptions.PackageNotFoundError: Package not found at 'Whats up dude ur not ugly always remember that'
>>> 
>>> #NICE IT ALL WORKS

>>> 
>>> 