s=input("Enter the string:")
chk,chknm=ord(s[0]),s[0]
for i in s:
    if ord(i)>chk:
        chknm=i
        chk=ord(i)
print(chknm,chk)
