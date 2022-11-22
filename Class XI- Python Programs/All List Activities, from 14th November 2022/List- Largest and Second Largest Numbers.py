n=int(input("Enter the number of terms:"))
l=[]
for i in range(n):
    l.append(int(input("Enter number "+str(i+1)+":")))
large=l[0]
for i in range(n):
    if l[i]>large:
        large=l[i]
for i in range(n):
    if l[i]!=large:
        sec=l[i]
        break
for i in range(n):
    if (l[i]!=large) and (l[i]>sec):
        sec=l[i]
print("The largest number is:",large)
print("The second largest number is:",sec)
        
