num1=int(input("enter num1 :"))
num2=int(input("enter num2 :"))
num3=int(input("enter num3 :"))
if num1>num2 and num1>num3:
    print("num1 is grater then num2 & 3")
elif num2>num1 and num2>num3:
    print("num2 is grater than num1 & 3")
elif num3>num1 and num3>num2:
    print("num3 is grater than num1 & 2")
else:
    print("enter valid number")