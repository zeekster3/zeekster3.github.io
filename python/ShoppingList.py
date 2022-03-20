
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
    elif choice == 3:
        print()
        index = int(input('Which item would you like to remove? '))
        print()
        del cart[index - 1]
        del prices[index - 1] 
        del quantities[index - 1]
    elif choice == 4:
        subtotal = 0
        print()
        for i in range(len(cart)):
            subtotal += prices[i] * quantities[i]
            tax = subtotal * .06
            total = subtotal + tax
        print(f'The total price of the items in the shopping cart is ${total:.2f}')
print("Thank you. Goodbye.")