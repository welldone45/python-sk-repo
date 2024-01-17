status=True

while status:
    menu=  '''

    1) First Name
    2) Username
    3) Email
    4) Password
    5) confirm Password'''

    print(menu)

    fname=input("Enter your firstname: ")
    username=input("Enter your username: ")
    email=input("Enter your email: ")
    password=input("Enter your password: ")
    cpassword=input("Enter your password: ")

    if password==cpassword:

        print("------------------------------")

        print("Your first name is:",fname)
        print("Your username name is:",username)
        print("Your email is:",email)
        print("Your password:",password)
        print("confirm password:",cpassword)
        print("------------------------------")
        print("User Register Successfully")
    else:
        print("Password and Confirm Does not Matched")

    choice=input("Do you want to register again? y for yes and n for no:")

    if choice=='n' or choice=='no':
        status=False