l=[]
n=int(input("Enter the number of terms you would like to check for:"))
for i in range(n):
    a=int(input("Enter number "+str(i+1)+":"))
    l.append(a)
print("The numbers you have entered are:",l)

for x in range(len(l)):
    if l[x]==0 or l[x]==1:
        print(l[x],"is neither a prime nor a composite number.")
    else:
        count=0
        for k in range(1,l[x]+1):
            if l[x]%k==0:
                count+=1
                
        if count==2:
            print(l[x],"is a prime number.")
        else:
            print(l[x],"is a composite number.")
