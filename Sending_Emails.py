Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #sending emails
>>> 
>>> import smtplib
>>> #smtplib stands for simple mail transfer protocol library
>>> 
>>> conn = smtplib.SMTP('smtp.gmail.com', 587)
>>> type(conn)
<class 'smtplib.SMTP'>
>>> #nice
>>> #conn variable stands for connection object
>>> # smtp.gmail.com is the server domain name of gmail
>>> # 587 is the usual port for emials
>>> 
>>> #lets connect now
>>> 
>>> conn.ehlo()
(250, b'smtp.gmail.com at your service, [120.29.75.230]\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8')
>>> #nice
>>> #status codes that are in the 200 range mean successful connection
>>> 
>>> #lets encrypt since were putting our password
>>> conn.starttls()
(220, b'2.0.0 Ready to start TLS')
>>> #nice
>>> #STARTTLS is an email protocol command that tells an email server that an email client, including an email client running in a web browser, wants to turn an existing insecure connection into a secure one.
>>> #Opportunistic TLS refers to extensions in plain text communication protocols, which offer a way to upgrade a plain text connection to an encrypted connection instead of using a separate port for encrypted communication. Several protocols use a command named "STARTTLS" for this purpose.
>>> 
>>> #nice since were encrypted now lets log in
>>> 
>>> conn.login('ndcrisologo@gmail.com', 'edenhazard10')
(235, b'2.7.0 Accepted')
>>> #Nice
>>> #lets send an email
>>> conn.sendmail('ndcrisologo@gmail.com', 'ndcrisologo@gmail.com', 'Subject: Python Email Test. \n\n Dear Chummi, \nyou're not ugly don't worry about things like that. \nRegards, \nChummi')
SyntaxError: invalid syntax
>>> #OOPS
>>> conn.sendmail('ndcrisologo@gmail.com', 'ndcrisologo@gmail.com', 'Subject: Python Email Test. \n\n Dear Chummi, \nyoure not ugly don't worry about things like that. \nRegards, \nChummi')
	      
SyntaxError: invalid syntax
>>> #OOPS
>>> 
>>> conn.sendmail('ndcrisologo@gmail.com', 'ndcrisologo@gmail.com', 'Subject: Python Email Test. \n\n Dear Chummi, \nyoure not ugly dont worry about things like that. \nRegards, \nChummi')
{}
>>> #the output of sendmail is a dictionary which includes all the errors
>>> #since its empty it means it was a succcess
>>> 
>>> #now lets logout
>>> 
>>> conn.exit()
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    conn.exit()
AttributeError: 'SMTP' object has no attribute 'exit'
>>> #OOPS
>>> 
>>> conn.quit()
(221, b'2.0.0 closing connection z20sm888479pfk.199 - gsmtp')
>>> #OKAY WERE GOOD YAYAYYAY
>>> 
>>> #note that u have to follow the format for sendmail
>>> #the third string shuld have both subject and body
>>> #Subject should be in Subject: text  format
>>> #end the subject by putting two newlines (\n\n)
>>> 
>>> #note that if you create a program to send multiple emails, you can probs send only a max of 100 a day w gmail. If you wanna send thousands, go for a mailing list service