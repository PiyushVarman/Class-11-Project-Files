l=[]
n=int(input("Enter the number of terms you want to enter:"))
for i in range(n):
    l.append(int(input("Enter number "+str(i+1)+":")))
l.sort()
print("The second largest number in the list",l,"is",l[-2])
