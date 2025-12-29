total_expense = 0


def calculate_expense():
    """Adds new expense or gives total expense sum"""

    def add_expense(expense_sum):
        """Adds new expense"""
        global total_expense
        total_expense += expense_sum
        print("Added successfully")

    def get_expense():
        """Gives total expense sum"""
        print(f"Your total expense sum is {total_expense}")
        return total_expense

    return add_expense, get_expense


add_expenses, get_expenses = calculate_expense()

while True:
    action = input(
        "Which action would you like to start? \n Enter '1' to add an expense or '2' to get total expense sum\n")

    if action == '1':
        expense = float(input("Enter sum of new expense\n"))
        add_expenses(expense)
    elif action == '2':
        get_expenses()
    else:
        print("Unknown operation")

    if input("Enter 'y' or 'yes' if you want to continue ").lower() not in ("yes", "y"):
        break
