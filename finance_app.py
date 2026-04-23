import os
print("Saved in folder:", os.getcwd())


print("Welcome to Personal Finance Assistant!")

expenses = []

# --- Load previous expenses from file ---
try:
    file = open("expenses.txt", "r")
    for line in file:
        amount, category = line.strip().split(",")
        expenses.append({"amount": float(amount), "category": category})
    file.close()
except:
    pass  # file doesn't exist yet

while True:
    print("\nMenu:")
    print("1. Add a new expense")
    print("2. View all expenses")
    print("3. Calculate total and average expense")
    print("4. Clear all expenses")
    print("5. Split a bill")
    print("6. Show category-wise spending")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            amount = float(input("Enter expense amount: ₹"))
            category = input("Enter category (Food, Travel, etc): ").capitalize()
            expenses.append({"amount": amount, "category": category})
            print("Expense added successfully!")
        except:
            print("Invalid input! Try again.")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            print("\nYour expenses:")
            for i in range(len(expenses)):
                exp = expenses[i]
                print(f"{i + 1}. ₹{exp['amount']} - {exp['category']}")

    elif choice == "3":
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            total = 0
            for expense in expenses:
                total += expense["amount"]
            average = total / len(expenses)
            print(f"Total expense: ₹{total}")
            print(f"Average expense: ₹{average}")

    elif choice == "4":
        expenses.clear()
        print("All expenses cleared.")

    elif choice == "5":
        try:
            bill_amount = float(input("Enter total bill amount: ₹"))
            tip_percentage = float(input("Enter tip percentage: "))
            tip_amount = (tip_percentage / 100) * bill_amount
            total_amount = bill_amount + tip_amount
            people = int(input("Enter number of people: "))
            amount_per_person = total_amount / people
            print(f"Total (including tip): ₹{total_amount}")
            print(f"Each person pays: ₹{amount_per_person}")
        except:
            print("Invalid input! Try again.")

    elif choice == "6":
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            category_totals = {}

            for exp in expenses:
                category = exp["category"]
                amount = exp["amount"]

                if category in category_totals:
                    category_totals[category] += amount
                else:
                    category_totals[category] = amount

            print("\nCategory-wise spending:")
            for cat in category_totals:
                print(f"{cat}: ₹{category_totals[cat]}")

    elif choice == "7":
        # --- Save expenses before exiting ---
        file = open("expenses.txt", "w")
        for exp in expenses:
            file.write(f"{exp['amount']},{exp['category']}\n")
        file.close()

        print("Data saved. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")