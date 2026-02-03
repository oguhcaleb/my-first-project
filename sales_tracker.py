sales = []

while True:
    print("\n1. Add sale")
    print("2. View total sales")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Enter sale amount: "))
        sales.append(amount)
        print("Sale added.")
    elif choice == "2":
        print("Total sales:", sum(sales))
    elif choice == "3":
        break
    else:
        print("Invalid choice")
