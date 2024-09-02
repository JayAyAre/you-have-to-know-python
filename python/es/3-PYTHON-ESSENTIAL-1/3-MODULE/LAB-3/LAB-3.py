income = float(input("Enter the annual income: "))

if 0 < income < 85528:
    tax = income * .18 - 556.2
elif income >= 85528:
    tax = 14839.2 + income * .32
else:
    tax = 0

if tax < 0:
    tax = 0
tax = round(tax, 1)
print("The tax is:", tax, "thalers")
