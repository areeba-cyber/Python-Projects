expenses = []

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Total expense")
    print("4. End")

    choice = input("Enter your choice :")
    if choice == "1":
        expense_name  = input("Add your expense :")
        expense_amount = float(input("Add expense amount :"))

        expense = {
            "expense_name": expense_name,
            "expense_amount": expense_amount
        }

        expenses.append(expense)
        print("Expense Added Successfully!")

    elif choice == "2":
        print("\n These are the expenses :")

        if len(expenses) == 0:
            print("There is no expense in the list")
        else :
            for expense in expenses:
                print(f"{expense['expense_name']} - Rs{expense['expense_amount']}")

    
    elif choice == "3":
        total = 0
         
        for expense in expenses:
             total += expense["expense_amount"]
             print(f"\nTotal Expense = Rs {total}")
             

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid Choice!")
             



