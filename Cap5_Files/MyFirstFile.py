# with open("myFirstFile.txt", "w") as file:
#    file.write("Hakuna Matata!")
#

# with open("myFirstFile.txt", "a") as file:
#    file.write("\nHakuna Matata2!")
#

# with open("myFirstFile.txt", "r") as file:
#     content = file.read()
#     print(content)

with open("myFirstFile.txt", "r") as file:
    for line in file.readlines():
        print(line)
