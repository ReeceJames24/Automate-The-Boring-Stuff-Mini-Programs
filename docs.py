Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #reading and editing word document
>>> 
>>> import docx
>>> #lets open the document i just saved on d desktop
>>> 
>>> doc = docx.Document('/Users/chummi/Desktop/demo.docx')
>>> #paragraph member variable contains a list of paragraph objects in the file
>>> doc.paragraphs
[<docx.text.paragraph.Paragraph object at 0x10db99310>, <docx.text.paragraph.Paragraph object at 0x10db990d0>, <docx.text.paragraph.Paragraph object at 0x10db99100>, <docx.text.paragraph.Paragraph object at 0x10db99040>, <docx.text.paragraph.Paragraph object at 0x10db991c0>, <docx.text.paragraph.Paragraph object at 0x10db990a0>, <docx.text.paragraph.Paragraph object at 0x10db99250>]
>>> doc.paragraphs[0]
<docx.text.paragraph.Paragraph object at 0x10db992b0>
>>> #the paragaph objects have a text member variable also
>>> doc.paragraphs[0].text
'DEMO'
>>> doc.paragraphs[1].text
''
>>> p = doc.paragraphs[1]
>>> p.runs
[]
>>> #runs refer to the style changes in that paragraph so none for DEMO
>>> #i updated the first paragraph to have sryle changes lets try now again
>>> 
>>> doc.paragraphs[0].text
'DEMO'
>>> #oops need   to reopen the file since made some changes
>>> d = docx.Document('/Users/chummi/Desktop/demo.docx')
>>> doc.paragraphs[0].text
'DEMO'
>>> #WAT
>>> #ayt head to docsPart2.py thanks
>>> 