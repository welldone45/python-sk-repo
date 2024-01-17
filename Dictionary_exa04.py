mainstatus = True
product = {}
status = True
customerstatus = True

menu = """

                            MENU
                PRESS 1 FOR PRODUCT MANAGER
                PRESS 2 FOR CUSTOMER

        """
while mainstatus:
    print(menu)

    choice = int(input("Enter your chioice : "))
    if choice == 1:
        while status:
            subdict = {}
            print("WELCOME TO PRODUCT MANEGER")
            print()

            productname = input("Enter product name : ")
            qty = int(input("Enter qty : "))
            price = int(input("Enter price : "))

            subdict['qty'] = qty
            subdict['price'] = price

            product[productname] = subdict

            print(product)

            mchoice = input("do you want to continue press y for yes n for no : ").lower()
            if mchoice == 'y':
                status = True
            else:
                status = False

    else:
        while customerstatus:
            print("WELCOME TO CUSTOMER")
            print()

            for k,v in product.items():
                print(f"{k},",product[k]['price'])
                print()

                
            c_choice = input("do you want to continue press y for yes n for no : ").lower()
            if c_choice == 'y':
                customerstatus = True
            else:
                customerstatus = False        


            cchoice = input("do you want to continue press y for yes n for no : ").lower()
            if cchoice == 'y':

                mainstatus = True
            else:
                mainstatus = False


