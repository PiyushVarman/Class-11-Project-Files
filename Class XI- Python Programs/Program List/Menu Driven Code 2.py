sel=int(input('''Sum of 'n' natural numbers-1
Multiplication of a number 'm' with its 'n' multiples-2
Exit-3
Enter Your desired option.''')) #Sel=Selector.

#Sum of 'n' natural numbers:
if sel==1:
    n=int(input("Enter the number of natural numbers to be added:"))
    s=0
    for i in range(1,n+1):
        s+=i
    print("The sum of the natural numbers till",n,"is",s)

#Multiplying 'm' with 'n':
if sel==2:
    m=int(input("Enter the number to be multiplied:"))
    n=int(input("Enter the number of multiples of the number:"))
    for i in range(1,n+1):
        print(m,"times",i,"is:",m*i)

#ExIt, ExIt NoW:    
if sel==3:
    print("Come back later!")
