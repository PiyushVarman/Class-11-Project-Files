#Reversing a given number
n=int(input("Enter a number to be reversed."))
rev=0
rem=0
num=n #To save the number, unmodified.
while n!=0:
    rem=n%10 
    rev=rev*10+rem #This is to add parts of the reversed number to an empty variable
    n//=10  #This will reduce the digits of the number
print("The reversed number of",num,"is:",rev)


#To check if the number is a palindrome:
if rev==num:
    print("The given number is a palindrome.")
else:
    print("The given number is not a palindrome.")
