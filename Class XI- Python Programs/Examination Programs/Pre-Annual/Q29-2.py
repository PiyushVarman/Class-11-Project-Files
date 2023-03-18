d1={}
n=int(input("Enter the number of terms:"))
for i in range(n):
    na=input("Enter the name:")
    age=int(input("Enter "+na+"'s age:"))
    d1[na]=age
chk=input("Enter the substring:")
l=[]
for i in d1.keys():
    if chk in i:
        l.append(i)
if len(l)==0:
    print("The substring does not exist.")
else:
    for i in l:
        print(i)
