n=int(input("Enter the number of terms you want to enter:"))
l,o,e=[],0,0
for i in range(n):
    l.append(int(input("Enter number "+str(i+1)+":")))

for j in range(len(l)):
    if l[j]%2==0:
        e+=l[j]
    else:
        o+=l[j]

print("The sum of even numbers is:",e)
print("The sum of odd numbers is:",o)
