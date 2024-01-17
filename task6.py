side1=float(input("Enter the length of side 1 : "))
side2=float(input("Enter the length of side 2 : "))
side3=float(input("Enter the length of side 3 :"))
print("length 1 is :" "length 2 is :" "length 3 is :",side1,side2,side3)
if side1==side2==side3:
    print("Tringle is Equilateral")
elif side1==side2 or side1==side3 or side2==side3:
    print("Isoscales Tringle")
else:
    print("Scalene Tringle")     