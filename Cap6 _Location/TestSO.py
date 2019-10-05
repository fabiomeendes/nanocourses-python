import platform
import getpass
from datetime import datetime

print("Machine name:......", platform.node())
print("Architecture:......", platform.architecture())
print("SO:................", platform.system())
print("SO version:........", platform.release())
print("Processor:.........", platform.processor())
print("Python Version:....", platform.python_version())

print("\n-------------------------------------------\n")

print(datetime.now())

print("\n-------------------------------------------\n")

user = getpass.getuser()
password = getpass.getpass("Type your password")

if user == 'Usuário' and password == 'Hello':
    print('Welcome')
else:
    print('BLOCKED')

