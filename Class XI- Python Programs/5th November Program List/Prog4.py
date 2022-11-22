#Using variable method
n=int(input("Enter the number of terms you want to enter:"))
l,s=[],0
for i in range(n):
    l.append(int(input("Enter number "+str(i+1)+":")))
print("The maximum value of the list",l,"is:",max(l))
