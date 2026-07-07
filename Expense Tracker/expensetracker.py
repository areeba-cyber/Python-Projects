expenses = []

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Total expense")
    print("4. End")

    choice = input("Enter your choice :")
    if(choice == 1):
        expense_name  = input("Add your expense :")
        expense_amount = float(input("Add expense amount :"))

        expense = {
            expense_name : "expense_name",
            expense_amount: "expense_amount"
        }

        


