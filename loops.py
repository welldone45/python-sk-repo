'''
Loops

1) for loops:- sequence controlled loop
range(starting range, ending range,jump):- To find the range between the number

Code suggestions
'''
'''
for i in "Python":
    print(i)
'''

'''
for i in range(1,11):
    print(i)
'''

'''
for i in range(1,101):
    print(i)
'''


'''
for i in range(2,21,2):
    print(i)
'''

'''
for i in range(1,21,2):
    print(i)

'''
'''
for i in range(10,0,-1):
    print(i)
'''
'''number=int(input("Enter the number: "))
print("you have entered number: ",number)'''
'''
for i in range(1,number+1):
    print(i)
'''
'''
num=int(input("enter number"))
sum=0

for i in range(1,num+1):
    sum=sum+i # 0+1+2+3+4+5
print("sum=",sum)
'''
'''num=int(input("enter a  number:"))
evensum=0
oddsum=0

for i in range(1,num+1):
    if(i%2==0):
        evensum=evensum+i
    else:
        oddsum=oddsum+i
print("Evensum",evensum)
print("oddsum=",oddsum)'''

'''num=int(input("enter number:"))
f=1
for i in range(1,num+1):
    f=f*i #1*1*2*3*4*5
print("Factorial=",f)'''

num=int(input("enter number"))
num1=0
num2=1

print(num1)
print(num2)


for i in range(2,num+1):
    num3=num1+num2
    print(num3)
    num1=num2
    num2=num3


'''num=int(input("enter number"))


for i in range(1,11):
    print(num,"*",i,"=",num*i)
'''    


