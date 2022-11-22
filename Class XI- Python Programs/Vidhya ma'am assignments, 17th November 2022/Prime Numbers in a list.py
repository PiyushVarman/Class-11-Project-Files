n=int(input("Enter the number of terms:"))
l=[]
for i in range(n):
    l.append(int(input("Enter number "+str(i+1)+":")))

count=0
print("The prime numbers in the list",l,"are: ",end='')
for i in range(len(l)):
    a=0
    for j in range(1,l[i]+1):
       if l[i]%j==0:
           a+=1
    if a==2:
        count+=1
        print(l[i],',',end='',sep='')

print()
print("There are",count,"prime numbers in the given list.")
           
