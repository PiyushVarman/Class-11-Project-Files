l=[]
n=int(input("Enter the number of strings:"))
for i in range(n):
    l.append(input("Enter string "+str(i+1)+":"))
print()

chk=0
z=[]
for i in l:
    if len(i)>=chk:
        z.append(i.upper())
        chk=len(i)

for i in z:
    print(i)
