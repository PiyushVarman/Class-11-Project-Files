n=int(input("Enter the number of terms:"))
l=[]
for i in range(n):
    l.append(int(input("Enter the number:")))
k=l
for i in range(len(l)):
    for j in range(i,n):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print("The list in ascending order is:",l)

for i in range(len(l)):
    for j in range(i,n):
        if k[i]<k[j]:
            k[i],k[j]=k[j],k[i]
print("The list in descending order is:",k)
            


