n=int(input("Enter the number:"))
s=1
for i in range(1,n+1):
    fac=1
    for j in range(1,i+1):
        fac*=j
    s+=(i/fac)
    
print(s)
    
