n=int(input("Enter the number of terms:"))
l=[]
for i in range(n):
    l.append(int(input("Enter number "+str(i+1)+":")))
pp=[]
for i in range(len(l)):
    a=str(l[i])
    if a==a[::-1]:
        count=0
        for j in range(1,l[i]+1):
            if l[i]%j==0:
                count+=1
        if count==2:
            pp.append(l[i])

print("The prime numbers which are also palindromes are:",pp)
            
