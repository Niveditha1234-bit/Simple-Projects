import pandas as pd
expenses = []
def view_details(data):
    if not data:
        print("No expenses found.")
    else:
        df = pd.DataFrame(data, columns=["Date", "Category", "Amount"])
        print(df)
def add_expense():
    date = input("Enter the date (DD-MM-YYYY): ")
    category = input("Enter the category: ")
    amount = float(input("Enter the amount: "))
    expenses.append((date, category, amount))
    print("Expense added!")
def view_expenses():
    if not expenses:
        print("No expenses found. Add an expense first.")
    else:
        for i, (date, category, amount) in enumerate(expenses, start=1):
            print(f"{i}. Date: {date}, Category: {category}, Amount: {amount}")
def total_expenses():
    total = sum(amount for date, category, amount in expenses)
    print(f"Total expenses: {total}")

print("\nExpense Tracker")
print("1. Add Expense")
print("2. View Expenses")
print("3. Total Expenses")
print("4. Exit")
while True:
    choice = input("Choose an option: ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        total_expenses()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
view_details(expenses)