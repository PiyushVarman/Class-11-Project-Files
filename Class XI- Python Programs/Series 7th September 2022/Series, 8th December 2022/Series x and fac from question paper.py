n=int(input("Enter the number of terms:"))
x=int(input("Enter the x value:"))
fac,s=1,0
for i in range(1,n+1):
    if i%2!=0:
        fac*=i
        s+=(x**i)/fac
    if i%2==0:
        fac*=i
        s-=(x**i)/fac
print("The sum of all the terms are:",s)
        
        
