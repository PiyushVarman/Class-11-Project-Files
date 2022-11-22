x=int(input("Enter a number, so that I can tell you if it is odd or even and positive or negative."))
print("When divided by 2, the number is",x/2)
y=x/2

#Where x//2= X modulo(???) 2, where there will be no decimals in //.
#You can also use % for remainder.
if y==x//2:
    print("Hence, it is even.")
if y!=x//2:
    print("Hence, it is odd.")

if x<0:
    print("This number is negative as it is less than 0.")
if x>0:
    print("This number is positive as it is more than 0.")

input()
