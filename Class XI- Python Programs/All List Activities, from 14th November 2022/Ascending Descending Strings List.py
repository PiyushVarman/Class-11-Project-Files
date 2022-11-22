n=int(input("Enter the number of strings:"))
l=[]
for i in range(n):
    l.append(input("Enter string:"))

for i in range(len(l)):
    for j in range(len(l)):
        a=l[i].lower()
        b=l[j].lower()
        a,b=a[0],b[0]
        if ord(a)<ord(b):
            l[i],l[j]=l[j],l[i]
        
print(l)
