d=dict()
n=int(input("Enter the number of items:"))
i=1
chk,chknm=0,''
while i<=n:
    print()
    itemno=int(input("Enter the item number:"))
    itemna=input("Enter the item name:")
    itempr=int(input("Enter the item price:"))
    q=int(input("Enter the quantity of item:"))
    total=itempr*q
    b=(itemno,itemna,itempr,q,total)
    d[itemna]=b
    i+=1
    if total>chk:
        chk=total
        chknm=itemna
print("\nitem no\t","item name\t","item price\t","quantity\t","Total Amount\t")
for i in d[chknm]:
    print(i,end='\t')
print()
