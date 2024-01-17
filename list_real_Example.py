menu = """
         : : Jay Bhavani : : 

                MENU
            vadapav     RS.40
            dabeli      RS.30
            bhel        RS.75
            sandwich    RS.130
"""
cart = []   # blank list
qty_list = []   # qty list
price_list = []     # price list

status = True
while status:

    print(menu)

    product_name = input("Enter product which you want to buy : ").lower()
    qty = int(input("enter no.of qty you want ?"))
    price = 0

    if product_name == "vadapav":
        price = 40
    elif product_name == "dabeli":
        price = 30
    elif product_name == "bhel":
        price = 75
    elif product_name == "sandwich":
        price = 130

    cart.append(product_name)
    qty_list.append(qty)
    price_list.append(price)

    choice = input("do you want to purchase more item press y for yes and press n for no")
    if choice == 'y':
        status = True
    else:
        status = False

print("--------------------------")

for product in cart:
    # print(product)
    index_value = cart.index(product)
    
    qty_value = qty_list[index_value]
    
    price_value = qty_value * price_list[index_value]
    
    print(f"{product} Qty:{qty_value} = Rs.{price_value}")

remove_product_name = input("enter your product name which u want to remove : ")
r_index_value = cart.index(remove_product_name)
cart.pop(r_index_value)
qty_list.pop(r_index_value)
price_list.pop(r_index_value)

print("------------------------------")
# print(cart)
# print(qty_list)
# print(price_list)

for product in cart:
    #print(product)
    index_value = cart.index(product)
    qty_value = qty_list[index_value]
    price_value = qty_value * price_list[index_value]
    print(f"{product} Qty:{qty_value} = Rs.{price_value}")



'''menu = """
         : : Jay Bhavani : : 

                MENU
            vadapav     RS.40
            dabeli      RS.30
            bhel        RS.75
            sandwich    RS.130
"""
cart = []   # Blank list
qty_list = []   # Quantity list
price_list = []  # Price list

while True:
    print(menu)

    print("1. Add item to cart")
    print("2. Remove item from cart")
    print("3. Display Cart")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        product_name = input("Enter the product you want to buy: ").lower()
        qty = int(input("Enter the quantity you want: "))
        price = 0

        if product_name == "vadapav":
            price = 40
        elif product_name == "dabeli":
            price = 30
        elif product_name == "bhel":
            price = 75
        elif product_name == "sandwich":
            price = 130
        else:
            print("Invalid product name. Please choose from the menu.")
            continue

        cart.append(product_name)
        qty_list.append(qty)
        price_list.append(price)

    elif choice == '2':
        if not cart:
            print("Your cart is empty. Nothing to remove.")
            continue

        print("\n::: Shopping Cart :::")
        for i, (product, qty, price) in enumerate(zip(cart, qty_list, price_list), start=1):
            total_price = qty * price
            print(f"{i}. {product.capitalize()} Qty: {qty} = Rs.{total_price}")

        try:
            remove_index = int(input("Enter the number of the item you want to remove: ")) - 1
            if 0 <= remove_index < len(cart):
                removed_product = cart.pop(remove_index)
                qty_list.pop(remove_index)
                price_list.pop(remove_index)
                print(f"{removed_product.capitalize()} removed from the cart.")
            else:
                print("Invalid item number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    elif choice == '3':
        print("\n::: Shopping Cart :::")
        if not cart:
            print("Your cart is empty.")
        else:
            for product, qty, price in zip(cart, qty_list, price_list):
                total_price = qty * price
                print(f"{product.capitalize()} Qty: {qty} = Rs.{total_price}")

    elif choice == '4':
        print("Thank you for shopping. Exiting...")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")'''