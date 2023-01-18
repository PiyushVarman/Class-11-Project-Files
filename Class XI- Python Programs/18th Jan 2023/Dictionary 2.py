d=dict()
i=1
n=int(input("Enter the number of phone numbers:"))
while i<=n:
    print()
    name=input("Enter the name of the person:")
    city=input("Enter the city name:")
    pn=int(input("Enter the phone number:"))
    b=(city,name)
    d[pn]=b
    i+=1

l=d.keys()
for i in d:
    print("Phone number:",i)
    z=d[i]
    print('City\t',"Name\t")
    for j in z:
        print(j,end='\t')
    print()
        
print()
chk=int(input("Enter the number you want to check for:"))
if chk in l:
    print()
    print("Phone number",chk)
    z=d[chk]
    print("City\t","Name\t")
    for j in z:
        print(j,end='\t')
else:
    print("Sorry!",chk,"is not in the phone directory.")
