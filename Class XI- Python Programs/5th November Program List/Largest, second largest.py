l=[]
n=int(input("Enter the number of terms:"))
for i in range(n):
    l.append(int(input("Enter the number "+str(i+1)+":")))
large,second=l[0],0
for i in range(len(l)):
    if l[i]>large:
        second=large
        large=l[i]
print("The largest number in the list",l,"is",large)
print("The second largest number in the list",l,"is",second)
