#Simple Interest
p=int(input("Enter the Principal Amount:"))
r=float(input("Enter the Rate of Interest:"))
t=int(input("Enter the time of interest:"))
SI=p*r*t/100
A=SI+p
print("The simple interest is Rs.",SI)
print("The Amount is Rs.",A)
