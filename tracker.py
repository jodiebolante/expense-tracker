#Expense Tracker - Installment 5: The Menu Comes Alive
#Author: Jodie F. Bolante
#Shows setup, adding, view, total, invalid and exit.

print("=" * 40)
print(" " * 12 +"EXPENSE TRACKER")
print(" " * 6 +"Know where your money goes.")
print("=" * 40)
print()

name = input("What's your name? ")
tax_percent = float(input("Tax Rate %? "))
budget = float(input("Your budget? "))
print(f"Welcome, {name}!\n")

subtotal = 0
count = 0

while True:
    print("MAIN MENU")
    print(" " * 2 + "[1] Add an expense")
    print(" " * 2 + "[2] View all expenses\t\t(coming soon)")
    print(" " * 2 + "[3] Show total spent\t\t")
    print(" " * 2 + "[4] Exit")
    choice = input("Choose 1-4: ")

    if choice == "1":
        amount = float(input("Amount? "))
        subtotal += amount
        count += 1
        if amount > 200:
            print("  Huge expense - are you sure?")
        elif amount > 100:
            print("  Big expense.")
        elif amount > 50:
            print("  Moderate expense.")
        else:
            print("  Small expense.")
        
    elif choice == "2":
        print("Coming soon: the tracker can't remember each item yet.")
    
    elif choice == "3":
        tax = subtotal * (tax_percent/ 100)
        total = subtotal + tax
        left = budget - total
        print(f"  Expenses:\t{count}")
        print(f"  Subtotal:\t${subtotal}")
        print(f"  Tax ({tax_percent}%):\t${tax}")
        print(f"  Grand total:\t${total}")
        if total > budget:
            print(f"  Over budget by ${total - budget}!")
        elif total > budget * 0.90:
            print(f"  Careful: only ${left} left.")
        else:
            print(f"  Within budget. ${left} left.")
    elif choice == "4":
        print(f"Goodbye, {name}!")
        print("-" * 40)
        print("Made by: Jodie Bolante | Installment 5")
        print("=" * 40)
        break
    else:
        print("  Please choose 1, 2, 3 or 4.")











