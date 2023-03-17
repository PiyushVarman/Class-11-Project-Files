l=[]
while "end" not in l:
    s=input("Enter string:").lower()
    l.append(s)
for i in l:
    if i[0]==i[-1]:
        print(i)
