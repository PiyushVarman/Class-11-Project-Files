#Series 1
n=int(input("Enter number:"))
s=0
for i in range(1,n+1):
    s+=i #Adding all the terms to a single variable.
print("The sum of all the terms are:",s)

#Series 2
n=int(input("Enter number:"))
s=0 #Sum of terms
a=0
for i in range(1,n+1):
    s+=i
    a+=s #Sum of each number is added.
print(a,"is the sum of all the numbers.")

#Series 3
n=int(input("Enter number:"))
s=0 #Sum of terms
for i in range(1,n+1):
    s=i*i #Square of each number added.
print(s,"is the sum of squares of numbers.")

#Series 4
n=int(input("Enter number:"))
fac=1
d=0
for i in range(1,n+1):
    fac=fac*i
    d+=i/fac #Numerators divided by factorials are added.
print(d,"is the sum of numbers divided by factorials.")

#Series 5
x=int(input("Enter numerator value:"))
n=int(input("Enter number:"))
d=0
fac=1
for i in range(1,n+1):
    fac=fac*i
    d+=(x**i)/fac #Numerators (to the power of the element in a range) are divided by factorials and added to d.
print(d,"is the sum of all the numbers divided by factorials.")

#Series 6
x=int(input("Enter numerator value:"))
n=int(input("Enter number:"))
d=0
fac=1
for i in range(1,n+1):
    fac=fac*i
    if i%2==0:
        d+=(x**i)/fac #Odd nos. are added.
    else:
        d-=(x**i)/fac #Even nos. are subtracted.
print(d,"is the sum of this series.")

#Series 7
n=int(input("Enter the ending number:"))
x=int(input("Enter the x value:"))
fac=1
s=1
for i in range(2,n+1):
    if i%2==0:
        fac*=i #Odd nos. are ignored, but the factorial value MUST be updated.
    else:
        fac*=i
        s+=(x**(i-1))/fac #Even number combinations are added to a certain variable.
print("The answer is:",s)
    
