#Gmail Email Sender


import sys
#TO DO: Connect to smtp server
print('Initializing..')
for i in range(1,30000):
    if i == 300000:
        print('Initialized')
import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()

#TO DO: Log-In 
ea = str(input("Enter email address (note:case sensitive):"))
pas = str(input("Enter password (note:case sensitive):"))
conn.starttls()
conn.login(ea,pas)

#TO DO: Collate recipients for conn.sendmail(ea,
recipient = input("Input recipient email address:")

#TO DO: Subject and Body
subj = str(input('Input Email Subject:')) + '\n\n'
body = str(input('Input Body:'))


#TO DO: Send Email
conn.sendmail(ea, recipient, str(subj) + str(body))
print('Email sent successfully')
print('Thank you for using Gmailer')
sys.exit() 
    
               
                  
    
                  
                  
                  


    
                     
                     
  
