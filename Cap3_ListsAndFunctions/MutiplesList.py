boyfriends = []
girlfriends = []
answer = "S"

while answer == "S":
    boyfriends.append(input("Boyfriend: "))
    girlfriends.append(input("Girlfriend: "))
    answer = input("Type \"S\" to continue: ").upper()

for index in range(0, len(boyfriends)):
    print("\nCouple......:", (index + 1))
    print("Boyfriend...:", (boyfriends[index]))
    print("Girlfriend..", (girlfriends[index]))
