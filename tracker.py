#Expense Tracker - Installment 3: The Tracker Does Math
#Author: Jodie F. Bolante
#Shows landing page, a running subtotal, tax as a percentage, and a yes/no budget check.
print("=" * 40)
print(" " * 12 +"EXPENSE TRACKER")
print(" " * 6 +"Know where your money goes.")
print("=" * 40)
print()
print("MAIN MENU")
print(" " * 2 + "[1] Add an expense\t\t(coming soon)")
print(" " * 2 + "[2] View all expenses\t\t(coming soon)")
print(" " * 2 + "[3] Show total spent\t\t(coming soon)")
print(" " * 2 + "[4] Exit\t\t\t(coming soon)\n")
name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.\n")
subtotal = 0
item1 = input("First expense? ")
amount1 = float(input("Amount? "))
subtotal += amount1
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal += amount2
tax_percent = float(input("Tax Rate %? "))
tax = subtotal * (tax_percent / 100)
total = subtotal + tax
budget = float(input("Your budget? "))
over_budget = total > budget
left = budget - total
print()
print("-" * 40)
print("SUMMARY")
print(f"  - {item1}: \t${amount1}")
print(f"  - {item2}: \t${amount2}")
totalSpent = amount1 + amount2;
average = totalSpent/ 2;
print(f"Subtotal:\t${subtotal}")
print(f"Average:\t${average}")
print(f"Tax (12.0%):\t${tax}")
print(f"Grand Total:\t${total}")
print(f"Over budget?\t{over_budget}")
print(f"Left in budget:\t${left}")
print("-" * 40)
print("Made by: Jodie Bolante | Installment 3")



