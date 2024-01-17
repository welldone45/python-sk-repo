def findFactorial(num):
    f = 1
    for i in range(1,num+1):
        f*=i

    return f

number = int(input("enter a number : "))

ans = findFactorial(number)
print("ans = ",ans)