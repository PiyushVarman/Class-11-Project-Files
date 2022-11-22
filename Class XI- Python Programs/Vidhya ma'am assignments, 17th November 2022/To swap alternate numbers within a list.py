n=int(input("Enter the number of terms:"))
l=[]
for i in range(n):
    l.append(int(input("Enter number "+str(i+1)+":")))

print("The list is",l)
j=0

while j<len(l)-2:
    l[j],l[j+2]=l[j+2],l[j]
    j+=3

print("The list is",l)
