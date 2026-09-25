#==========================================
#       STUDENT EXPENSE TRACKER
# ==========================================

# Empty list to store all expenses
expenses = []


# ------------------------------------------
# 1. ADD EXPENSE
# ------------------------------------------

def add_expense():

    print("\n----- Add Expense -----")

    category = input("Enter category: ")

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Please enter a valid amount.")
        return

    description = input("Enter description: ")

    expense = {
        "category": category,
        "amount": amount,
        "description": description
    }

    expenses.append(expense)

    print("Expense added successfully!")


# ------------------------------------------
# 2. VIEW ALL EXPENSES
# ------------------------------------------

def view_expenses():

    print("\n----- All Expenses -----")

    if len(expenses) == 0:
        print("No expenses found.")
        return

    for i in range(len(expenses)):

        print("\nExpense", i + 1)

        print("Category:",
              expenses[i]["category"])

        print("Amount: ₹",
              expenses[i]["amount"])

        print("Description:",
              expenses[i]["description"])


# ------------------------------------------
# 3. SEARCH EXPENSE
# ------------------------------------------

def search_expense():

    if len(expenses) == 0:
        print("\nNo expenses found.")
        return

    category = input(
        "\nEnter category to search: "
    )

    found = False

    for expense in expenses:

        if expense["category"].lower() == category.lower():

            print("\nCategory:",
                  expense["category"])

            print("Amount: ₹",
                  expense["amount"])

            print("Description:",
                  expense["description"])

            found = True

    if found == False:
        print("No expense found in this category.")


# ------------------------------------------
# 4. TOTAL EXPENSE
# ------------------------------------------

def total_expense():

    if len(expenses) == 0:
        print("\nNo expenses found.")
        return

    total = 0

    for expense in expenses:

        total = total + expense["amount"]

    print("\nTotal Expense = ₹", total)


# ------------------------------------------
# 5. HIGHEST EXPENSE
# ------------------------------------------

def highest_expense():

    if len(expenses) == 0:
        print("\nNo expenses found.")
        return

    highest = expenses[0]

    for expense in expenses:

        if expense["amount"] > highest["amount"]:

            highest = expense

    print("\n----- Highest Expense -----")

    print("Category:",
          highest["category"])

    print("Amount: ₹",
          highest["amount"])

    print("Description:",
          highest["description"])


# ------------------------------------------
# 6. DELETE EXPENSE
# ------------------------------------------

def delete_expense():

    if len(expenses) == 0:
        print("\nNo expenses found.")
        return

    view_expenses()

    try:

        number = int(
            input("\nEnter expense number to delete: ")
        )

        if number >= 1 and number <= len(expenses):

            deleted = expenses.pop(number - 1)

            print(
                "\nExpense deleted:",
                deleted["description"]
            )

        else:

            print("Invalid expense number.")

    except ValueError:

        print("Please enter a valid number.")


# ------------------------------------------
# 7. SAVE EXPENSES TO FILE
# ------------------------------------------

def save_expenses():

    file = open("expenses.txt", "w")

    for expense in expenses:

        data = (
            expense["category"]
            + ","
            + str(expense["amount"])
            + ","
            + expense["description"]
            + "\n"
        )

        file.write(data)

    file.close()

    print("\nExpenses saved successfully!")


# ------------------------------------------
# 8. MAIN MENU
# ------------------------------------------

while True:

    print("\n")
    print("====================================")
    print("       STUDENT EXPENSE TRACKER")
    print("====================================")

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Total Expense")
    print("5. Highest Expense")
    print("6. Delete Expense")
    print("7. Save Expenses")
    print("8. Exit")

    print("====================================")

    choice = input("Enter your choice: ")


    if choice == "1":

        add_expense()


    elif choice == "2":

        view_expenses()


    elif choice == "3":

        search_expense()


    elif choice == "4":

        total_expense()


    elif choice == "5":

        highest_expense()


    elif choice == "6":

        delete_expense()


    elif choice == "7":

        save_expenses()


    elif choice == "8":

        print("\nThank you for using")
        print("Student Expense Tracker!")

        break


    else:

        print("\nInvalid choice. Please try again.")