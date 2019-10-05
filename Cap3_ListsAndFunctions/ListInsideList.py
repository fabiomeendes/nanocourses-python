# Depreciation and Exclusion

eqList = []
answer = "S"

while answer == "S":
    eq = [
        input("Eq: "),
        float(input("Value: ")),
        int(input("Serial: ")),
        input("Department: ")
    ]
    eqList.append(eq)
    answer = input("\nType \"S\" to continue: ").upper()

for i in eqList:
    print("\nEq name.....:", i[0])
    print("Value.......:", i[1])
    print("Serial......:", i[2])
    print("Department..:", i[3])

eqToDepreciation = input("\nType a eq name to depreciate: ")
for i in eqList:
    if eqToDepreciation == i[0]:
        print("Old value:", i[1])
        i[1] = i[1] * 0.9
        print("Current value:", i[1])

serialToDelete = int(input("\nType a serial name to delete: "))
for i in eqList:
    if serialToDelete == i[2]:
        eqList.remove(i)

values = []
for i in eqList:
    values.append(i[1])

if len(values) > 0:
    print("\nThe most expensive equipment costs", max(values))
    print("The most cheapest equipment costs", min(values))
    print("The total of equipments is", len(values))
    print("The total price of equipments is", sum(values))


