
cart = []
choice = ''
print()

while choice != 5:
    print()
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove Item")
    print("4. Compute total")
    print("5. Quit")
    print()
    

    choice = int(input("Please enter an action: "))
    print()


    if choice == 1:
        item = input("What item would you like to add? ")
        cart.append(item)
        print()
        print(f"'{item}' has been added to the cart.")
        print()
    elif choice == 2:
        print()
        print("The contents of your shopping cart are: ")
        for item in cart:
            print(item)

print("Thank you. Goodbye.")