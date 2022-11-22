num=int(input("Enter a number to check if it is a prime."))
count=0
for i in range(1,num+1):
    if num%i==0:  #Remainder should be equal to 0, for i to be a factor.
        count+=1

print("The given number has",count,"factors.")

#since prime number has only 2 factors, 1 and itself.
if count >2:
    print("The given number",num,"is a composite number.")
elif count==2:
    print("The given number",num,"is a prime number.")
elif count==1 or count ==0:
    print("The given number",num,"is neither prime or composite.")
