def ask():
    return input("What do you want?\n" +
                 "<I> - To insert a user\n" +
                 "<S> - To search a user\n" +
                 "<D> - To delete a user\n" +
                 "<L> - To list a user: ").upper()


def insert(dictionary):
    dictionary[input("Type a login: ").upper()] = [
        input("Type a name: ").upper(),
        input("Type the last access date: "),
        input("Which was the last station accessed: ").upper()
    ]
    save(dictionary)


def save(dictionary):
    with open("bd.txt", "a") as file:
        for key, value in dictionary.items():
            file.write(key + ": " + str(value))
