x=input("Enter the string:")
l=[]
for i in range(len(x)):
    l.append(x[i])

j=0
while j<len(l)-1:
    if l[j]==l[j+1]:
        l.remove(l[j])
        l.remove(l[j])
        j=0
    else:
        j+=1

a=''

for i in range(len(l)):
    a+=l[i]
print("The string that remains, after removing all the repetitions is:",a)
