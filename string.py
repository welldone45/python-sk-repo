'''
strings:- string is a series of characters or a bunch of alphabets

tops
kamal
narendra

Single-line string --"",'',"""

Multiline string:-''' ''' 

string index value starts from 0.

'''
#      01234567890123456789012345678901   
mystr="Hello and Welcome to the Python!"

print(mystr)
# output:- Hello and Welcome to the Python!

# print(len(mystr)) length of string-len()
# print(mystr[0])
#print(mystr[5])
#print(mystr[23])
#print(mystr[15])
# -------- slicing of string:--------------
#print(mystr[0:8])
#print(mystr[10:22])
#print(mystr[-1])
#print(mystr[2:])
#print(mystr[:13])

'''for i in mystr:
    print(i)'''

#-----------------Inbuilt Methods---------------------------#

#print(mystr.capitalize()) Make first character in uppercase and in lowercase
#print(mystr.casefold())     Make all characters in lowercase
#print(mystr.count()) count the occurence of word or letter
#print(mystr.index("e")) to find the index value of letter or word
#print(mystr.lower()) into lowercase


# find the string length without function
'''count=0
mystr=input("enter the string:")

for i in mystr:
    count+=1
print("Count=",count)
'''

# b=78.34
#print(b)

# name="manav"
# print("Your name is ",name)

# print(15//4) floor division

# Palindrome

num=int(input("enter a number:"))
original_num=num
rev=0

while num>0:
    digit=num%10
    rev=rev*10 +digit
    num=num//10
print(rev)

if original_num==rev:
    print("Palindrome Number")
else:
    print("Not Palindrome Number")