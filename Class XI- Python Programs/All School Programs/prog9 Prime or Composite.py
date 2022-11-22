l=int(input("Enter the lower limit:")) #Lower limit
u=int(input("Enter the upper limit:")) #Upper limit

for z in range(l,u+1): #Controlling the range values.
    count=0  #Resetting factor count for EACH number
    for i in range(1,z+1):
        if z%i==0:  #If remainder 0, the number is divisible and is a factor.
            count+=1 #Increasing the factor count
    if count==2: #If ONLY 2 factors, then the number is prime
        print(z,end=',')
print("are prime numbers in this range.")
