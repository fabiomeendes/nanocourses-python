# The key is a tuple

users = {}
emails = ["fabio.camillo@asteria.com.br", "fabiocamillo@outlook.com"]

tuple01 = list(enumerate(emails))

print(tuple01)

for key in range(0, len(tuple01)):
    print("Email: ", tuple01[key][1])
    users[tuple01[key]] = [input("Type a name: "), input("Type the level: ")]

for key, data in users.items():
    print("\nUser...:", key[0])
    print("Email..:", key[1])
    print("Name...:", data[0])
    print("Level..:", data[1])
