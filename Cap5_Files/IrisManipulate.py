database = []

with open("iris.data", "r") as file:
    for register in file.readlines():
        database.append(register.split(","))

print(database)
print(database[0][0])
print(database[1][0])
print(float(database[0][0]) + float(database[1][0]))