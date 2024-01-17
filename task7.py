cost_prise=float(input("enter costing prise :"))
selling_prise=float(input("enter selling prise :"))

profit=selling_prise-cost_prise
lost=cost_prise-selling_prise

if profit>0:
    print("Profit")
elif lost>0:
    print("Lost")
else:
    print("No Profit, No Lost")    