n=int(input("Enter the number:"))
s=0
for i in range(1,n+1):
    fac=1
    for j in range(1,i+1):
        fac*=j
    if i%2!=0:
        s+=fac
    else:
        s-=fac
print(s)
