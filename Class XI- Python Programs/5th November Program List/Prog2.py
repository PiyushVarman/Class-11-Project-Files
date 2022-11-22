l=[]
n=int(input("Enter number of terms:"))
for i in range(n):
    l.append(int(input("Enter number "+str(i+1)+":")))
print("The list is",l)
j=0
while j<len(l):
    if l[j]%7==0 and l[j]!=l[-1]:
        l[j],l[j+1]=l[j+1],l[j]
        j+=2
    else:
        j+=1

print("The new list is:",l)
