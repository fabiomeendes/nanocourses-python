boyfriends = []
girlfriends = []
answer = "S"

while answer == "S":
    boyfriends.append(input("Boyfriend: "))
    girlfriends.append(input("Girlfriend: "))
    answer = input("Type \"S\" to continue: ").upper()

search = input("\nType the person name to search: ")

for i in range(0, len(boyfriends)):
    if search == boyfriends[i] or search == girlfriends[i]:
        print("Couple:", boyfriends[i], "and", girlfriends[i])
