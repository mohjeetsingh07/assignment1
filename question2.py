# Ask the user for their gross income and number of dependents
gross_income = float(input("Enter your gross income to the nearest penny: "))
num_dependents = int(input("Enter the number of dependents you have: "))


taxable_income = gross_income - 10000 - (num_dependents * 3000)


tax_owed = taxable_income * 0.2

print("Your taxable income is: $", taxable_income)
print("Your income tax owed is: $", tax_owed)
