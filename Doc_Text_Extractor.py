#doc text copier

import docx
import pyperclip
import random

x = 1 #for infinite looping

while x == 1:
    print('Input Root Path of docx file')
    filename = input()

    def DocCopier(filename):
        doc = docx.Document(filename)
        FullText = []
        for paragraph in doc.paragraphs:
            FullText.append(paragraph.text)
        return '\n'.join(FullText) #this will return the Fulltext list of strings after the iteration is complete and will slplit each string with a newline
    

    print(DocCopier(filename))
    pyperclip.copy(DocCopier(filename))

    for i in range(1, 700001):
        if i == 350000:
            print('Copying full text to clipboard....')
        if i ==700000:
            print('Full text has been copied to clipboard successfully')
        

    

