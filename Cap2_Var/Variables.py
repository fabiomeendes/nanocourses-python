name = input("Type an employee: ")
company = input("Type a company:")
qt_employees = int(input("Type employees quantity: "))
monthlyPaymentAverage = float(input("Type monthly payment average: "))

print(name + " works at " + company)
print("There are", qt_employees, "employees")
print("The average is", str(monthlyPaymentAverage))
print("The data type of [monthlyPaymentAverage] is", type(monthlyPaymentAverage))
