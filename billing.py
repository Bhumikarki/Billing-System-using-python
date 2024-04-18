while True:
    total = 0
    products = []  # List to store products
    
    while True:
        name = input("Enter name of product: ")
        amount = float(input("Enter amount of product: "))
        quantity = int(input("Enter number of product: "))
        total += amount * quantity
        products.append((name, amount, quantity))  # Store product details
        
        repeat = input('Do you want to add more items? (yes/no): ')
        if repeat== "no" or repeat == "NO":
            break
        print("-" * 50)    
    discount = 0

    # Ask for membership
    membership = input("Are you a member? (yes/no): ")
    if membership == "yes" or membership == "YES":
        phone_number = int(input("Enter your phone number for the membership card: ")) 
        discount = 0.01 * total  # Applying 1% discount for members

    print("-" * 50)    
        
    # Display total before discount
    print("Total amount before discount:", total)
    
    # Display discount amount
    print("Discount amount:", discount)
    
    # Apply discount
    total -= discount
    print("Amount to be paid after discount:", total)

    print("-" * 50)
    print("***** Happy Shopping *****")

    repeat_order = input("Do you want to start a new order? (yes/no): ")
    if repeat_order == "no" or repeat_order=="NO":
        break
