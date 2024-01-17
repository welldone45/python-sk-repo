name=input("Enter your name : ")
print("Your Name is : ",name)

age=int(input("Enter your age:"))
print("your age is :",age)

std=int(input("Enter your std : "))
print("you are in std : ",std)

maths=float(input("enter Maths marks:"))
print("Maths:",maths)

Science=float(input("enter Science marks :"))
print("Science",Science)

English=float(input("enter English marks:"))
print("English :",English)

total= (maths+Science+English)
percentage= (total*100/300)
print("percentage is : ",percentage)

if percentage>70:
    print(" ::: Distinction ::: ")
elif percentage>=65 and percentage<70:
    print(" :: 1st Class :: ")
elif percentage>=60 and percentage<65:
    print(" : 2nd Class :")
elif percentage>=55 and percentage<60:
    print("3rd Class")
elif percentage<55:
    print("Fail")