num1=int(input("Enter the number to check if it is perfect."))
count=0
for i in range(1,num1+1):
    if num1%i==0:
        count+=i

if count==2*num1:
    print("This is a perfect number.")
else:
    print("This is not a perfect number.")

input()

