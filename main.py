from expences import add_expences , display_expenses , delete_expense

while True:

    print("1. Add Expence")
    print("2. Display Expence")
    print("3. Delete Expence")
    print("4. Update Expense")
    print("5. Exit")
    
    chooise = input("enter your choise")

    if chooise == '1':
        add_expences()

    elif chooise == '2':
        display_expenses()

    elif chooise == '3':
        delete_expense()

    elif chooise == '4':
        pass

    elif chooise == '5':
        break