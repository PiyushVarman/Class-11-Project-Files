n=int(input("Enter the number of terms:"))
l=[]
for i in range(n):
    l.append(int(input("Enter number "+str(i+1)+":")))
an=[]
for i in range(len(l)):
    a=str(l[i])
    chk=l[i]
    sumchk=0
    while l[i]>0:
        rem=l[i]%10
        l[i]=l[i]//10
        sumchk+=(rem**len(a))
    if sumchk==chk:
        an.append(chk)

print("The Armstrong numbers are:",an)
        

    
