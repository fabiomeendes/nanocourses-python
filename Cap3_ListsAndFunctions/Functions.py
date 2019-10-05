def fillEqList(eqList):
    answer = "S"
    while answer == "S":
        eq = [
            input("\nEq: "),
            float(input("Value: ")),
            int(input("Serial: ")),
            input("Department: ")
        ]
        eqList.append(eq)
        answer = input("\nType \"S\" to continue: ").upper()


def deprecateEq(eqList):
    eqToDepreciation = input("\nType a eq name to depreciate: ")
    percentage = int(input("\nType a percentage: "))
    for i in eqList:
        if eqToDepreciation == i[0]:
            print("Old value:", i[1])
            i[1] = i[1] * (1-percentage/100)
            print("Current value:", i[1])


def eqToDeleteBySerial(eqList):
    serialToDelete = int(input("\nType a serial name to delete: "))
    for i in eqList:
        if serialToDelete == i[2]:
            eqList.remove(i)
    return "Excluded!"


def showList(eqList):
    for eq in eqList:
        print("\nEq name.....:", eq[0])
        print("Value.......:", eq[1])
        print("Serial......:", eq[2])
        print("Department..:", eq[3])
