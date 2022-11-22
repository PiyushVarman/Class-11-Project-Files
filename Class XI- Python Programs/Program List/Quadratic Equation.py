a=int(input("Enter the coefficient of x2:")) #X-Squared
b=int(input("Enter the coefficient of x:"))  #X
c=int(input("Enter the constant value:"))    #C
D=(b**2-(4*a*c))
print("The discriminant is",D)

s1,s2=(-b+(D**0.5))/(2*a),(-b-(D**0.5))/(2*a) #The +- Formula
if D>0:
    print("There are 2 real roots for this equation, they are",s1,"and",s2)
elif D<0:
    print("There are no real roots for this equation.")
elif D==0:
    print("There are 2 equal roots for this equation, they are:",s1,"and",s2)

