num=int(input("Enter a number to check if it is a perfect number."))
count=0
for i in range(1,num+1):
    if num%i==0:  #Remainder should be equal to 0, for i to be a factor.
        count+=i

print("The sum of the factors of given number is",count)

if count==2*num:
    print("The given number",num,"is a perfect number.")
else:
    print("The given number",num,"is not a perfect number.")
