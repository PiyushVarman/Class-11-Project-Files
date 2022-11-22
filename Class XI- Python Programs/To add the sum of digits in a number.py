#Adding the sum of digits of a given number
n=int(input("Enter a number to be reversed."))
sum_=0
num=n #To save the number, unmodified.
while n!=0:
    sum_+=n%10 
    n//=10  #This will reduce the digits of the number
print("The sum of the digits of the given number",num,"is:",sum_)
