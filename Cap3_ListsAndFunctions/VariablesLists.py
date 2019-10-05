myList = []
answer = "S"

while answer == "S":
    myList.append(input("Girlfriend name: "))
    myList.append(input("Boyfriend name: "))
    answer = input("Type \"S\" to continue: ").upper()

for elem in myList:
    print(elem)
