from ftplib import *

ftp = FTP('ftp.ibiblio.org')  # computer address
print(ftp.getwelcome())

user = input('Type the user: ')
password = input('Type the password: ')
ftp.login(user, password)

print('Current directory: ', ftp.pwd())

ftp.cwd('pub')  # change directory to save the Files

print('Current directory: ', ftp.pwd())

print(ftp.retrlines('LIST'))

ftp.quit()
