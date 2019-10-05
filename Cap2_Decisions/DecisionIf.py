name = input("Type a name: ")
age = int(input("Type an age: "))
contagiousDisease = input("Contagious disease? ").upper()

if age > 65:
    print("The patient " + name + "has priority service.")
elif contagiousDisease == "SIM" or contagiousDisease == "YES":
    print("Go to the emergency room now!")
else:
    print("The patient doesn't has priority service.")
