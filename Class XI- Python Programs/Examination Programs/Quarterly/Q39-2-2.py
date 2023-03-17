l=int(input("Enter the lower limit:"))
u=int(input("Enter the upper limit:"))
a,b=-1,1
z=[]
for i in range(u):
    s=a+b
    a=b
    b=s
    z.append(s)
for i in range(l,u+1):
    if i in z:
        print(i)
