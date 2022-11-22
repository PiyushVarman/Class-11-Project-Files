x=int(input("Enter a number, so that I can tell you if it is odd or even."))
print("When divided by 2, the number is",x/2)
y=x/2

#Where x//2= X modulo(???) 2, where there will be no decimals in //.
if y==x//2:
    print("Hence, it is even.")
if y!=x//2:
    print("Hence, it is odd.")
