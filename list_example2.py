'''
store data in list

there are 3 ways store data in list

1) append() : to add data in existing  list
2) extend() : to add multiple data in existing list
3) insert() : to add specific data in existing list at specific position

'''

mylist = ["c","c++","python"]
print(mylist)

'''mylist.append("flutter")
print(mylist)

mylist.extend(["php","react"])
print(mylist)

mylist.insert(1,"node js")
print(mylist)
'''


mylist=[]

for i in range(1,6):
    name=input("enter a name : ")
    mylist.append(name)
print(mylist)





