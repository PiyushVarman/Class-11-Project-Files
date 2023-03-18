n=int(input("Enter the number of garments:"))
d={}
for i in range(n):
    zd={}
    gid=input("Enter the garment ID:")
    zd["type"]=input("Enter the type of the garment:")
    zd["material"]=input("Enter the material of the garment:")
    zd["unit price"]=int(input("Enter the unit price:"))
    d[gid]=zd
print(d)
for i in d.keys():
    if d[i]["material"]=="cotton":
        d[i]["unit price"]+=75
print(d)
