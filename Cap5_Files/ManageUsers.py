from Cap5_Files.Functions import *

users = {}
option = ask()

while option == "I" or option == "P" or option == "E" or option == "L":
    if option == "I":
        insert(users)
    print(users.items())
    option = ask()

    #
    # do delete File
    # do list File
