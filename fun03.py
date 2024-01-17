# function with parameters and function without return type

'''def checkEvenOdd(number) : # here, number is a parameter
    if number%2 == 0:
        print("Evern Number")
    else:
        print("Odd number")
num = int(input("ener a number:"))
checkEvenOdd(num)'''


#function with parameters with
def sum(num1,num2):
    ans = num1+num2
    print(ans)
def mul(num1,num2):
    ans = num1*num2
    print(ans)

n1 = int(input("enter number : "))
n2 = int(input("enter number : "))

menu = """

        press 1 for addition
        press 2 for multiplication
        press 3 for substraction
        press 4 for division
"""
print(menu)
choice = int(input("enter your choice"))

if choice == 1:
    sum(n1,n2)
elif choice == 2:
    mul(n1,n2)