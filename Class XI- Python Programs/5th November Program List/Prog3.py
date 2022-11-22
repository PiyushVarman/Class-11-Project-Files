l=[]
n=int(input("Enter the number of terms you want to enter:"))
for i in range(n):
    l.append(int(input("Enter Number "+str(i+1)+":")))
l.sort()
print("The sorted list is:",l)
