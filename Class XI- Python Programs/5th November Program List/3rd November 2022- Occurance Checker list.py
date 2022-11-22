l=[]
n=int(input("Enter the number of terms:"))
for i in range(n):
    a=int(input("Enter number "+str(i+1)+":"))
    l.append(a)
for j in range(len(l)):
    count=0
    for k in range(len(l)):
        if l[j]==l[k]:
            count+=1

    print(l[j],"occurs",count,"time(s)")
