import re

phoneNumRegex = re.compile(r'\d\d\d\d-\d\d\d\-\d\d\d\d')
# re.compile allows you to store the string as a regex object
# r allows you to bypass the \ since you ned to use \ a lot in regex

x = 1

while x == 1:
    regexError = False
    print('Input Statement')
    message = str(input())
    mo = phoneNumRegex.findall(message)
    
    while regexError == False:
        if str(mo) == '[]':
            print('Phone number not found')
            regexError = True #this will stop the while loop reenter the very first while loop (x == 1)
        else:
            print('Phone numbers found: ' + str(mo))
            regexError = True #this will stop the while loop and reenter the very first while loop (x == 1)
            
        
            
                
# ITS FINALLY WORKING IM GOING TO CRY TYG     

        





                           
