n=input("Enter the name of the owner:")
con=int(input("Enter "+n+"'s consumption:"))
if con>750:
    r=3.50
    up=con*r
elif con>=200:
    r=2.75
    up=con*r
else:
    r=1.50
    up=con*r
print("Name of the owner:",n)
print("Number of units:",con)
print("Charge per unit:",r)
print("Total amount:",up)
