'''
database

'''

name = "salim"
email="salim@gmail.com"
password="123456"

print(" Welcome to tops technologies")

u_email=input("enter your mail : ")
u_password=input("enter your password : ")

if u_email != email and u_password != password:
    print("Email and password both are incorrect")
elif u_email != email :
    print("Invalid email")
elif u_password != password :
    print("invalid password")
else:
    print("Welcome",name)