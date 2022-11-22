l=[]
n=int(input("Enter the number of terms:"))
for i in range(n):
    l.append(int(input("Enter the number "+str(i+1)+":")))
least,second=l[0],0
for i in range(len(l)):
    if l[i]<least:
        second=least
        least=l[i]
print("The least number in the list",l,"is",least)
print("The second least number in the list",l,"is",second)
