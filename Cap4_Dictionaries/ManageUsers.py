from Cap4_Dictionaries.Functions import *

users = {}
option = ask()

while option == "I" or option == "P" or option == "E" or option == "L":
    if option == "I":
        insert(users)
    print(users.items())
    option = ask()

    #
    # do delete
    # search
    # list
    #
    # Methods:
    # items()
    # values()
    # keys()
    # clear()
    # popItem() - remove a data and you can to manipulate
