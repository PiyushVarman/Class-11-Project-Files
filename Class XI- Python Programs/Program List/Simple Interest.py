p=int(input("Enter the principal amount in Rs:"))
r=float(input("Enter the rate of interest in %:"))
t=int(input("Enter the time period:"))
SI=p*r*t/100
A=SI+p
print("The simple interest is Rs.",SI)
print("The amount is Rs.",A)
