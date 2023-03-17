l=int(input("Enter the lower limit:"))
u=int(input("Enter the upper limit:"))
for i in range(l,u+1):
    count=0
    a=str(i)
    for j in range(len(a)):
        if a[j]==a[-(j+1)]:
            count+=1
    if count==len(a):
        print(i)
