#Expense Tracker - Installment 2: Talking to the User
#Author: Jodie F. Bolante
#Shows the landing, asks for two expenses, prints a summary.
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
print(f"Welcome, {name}! Let's log two expenses.")
print()
item1 = input("First expense? ")
amount1 = float(input("Amount? "))
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
print()
print("-" * 40)
print("SUMMARY")
print(f"  - {item1}: \t${amount1}")
print(f"  - {item2}: \t${amount2}")
totalSpent = amount1 + amount2;
average = totalSpent/ 2;
print(f"Total spent:\t${totalSpent}")
print(f"Average:\t${average}")
print("-" * 40)
print("Made by: Jodie Bolante | Installment 2")



