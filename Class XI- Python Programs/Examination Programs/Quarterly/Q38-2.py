n=input("Enter the octal number:")
s=0
for i in range(len(n)):
    s+=int(n[-(i+1)])*(8**i)
print(s)
