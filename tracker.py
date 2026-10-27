#Expense Tracker - Installment 4: The Tracker Makes Decisions
#Author: Jodie F. Bolante
#Shows landing page, a greeting, expenses and summary.

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

if amount1 > 200:
    print("  Huge expense - are you sure?")
elif amount1 > 100:
    print("  Big expense.")
elif amount1 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal += amount2

if amount2 > 200:
    print("  Huge expense - are you sure?")
elif amount2 > 100:
    print("  Big expense.")
elif amount2 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

if amount1 > 100 and amount2 > 100:
    print("  Two big expenses in a row - slow down!")

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
print(f"Tax ({tax_percent}%):\t${tax}")
print(f"Grand Total:\t${total}")

if total > budget:
    over_budget = total - budget
    print(f"Over budget by ${over_budget}!")
elif total > budget * 0.90:
    print(f"Careful: only ${left} left.")
else:
    print(f"Within budget. ${left} left.")

print("-" * 40)
print("Made by: Jodie Bolante | Installment 4")



