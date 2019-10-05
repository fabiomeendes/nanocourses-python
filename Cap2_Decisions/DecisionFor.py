number = int(input("Type a number for your multiplication table: "))
print("Number", number, "times tables")

for value in range(1, 11, 1):
    print(str(number), "x", str(value), "=", str(number*value))

