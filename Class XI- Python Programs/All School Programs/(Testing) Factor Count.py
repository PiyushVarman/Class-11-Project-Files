x=int(input("Enter the number you want to check the number of factors for"))
count=0
for i in range(1,x+1):
    if x%i==0:
        count+=1
print("The number of factors for",x,"is",count)
if count==2:
    print("This is a prime number.")
if count>2:
    print("This is a composite number.")
if count==1:
    print("This is neither a prime nor a composite number.")

input()
