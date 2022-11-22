'''#EXPERIMENTAL??
yr=int(input("Enter the year:"))

if yr%4==0 and yr%400==0:
    print("This is a leap year.")
elif yr%4==0 and yr%100!=0:
    print("This is a leap year.")
elif yr%4!=0:
    print("This is not a leap year.")
elif yr%4==0 and yr%100==0 and yr%400!=0:
    print("This is not a leap year.")
'''
#Nested If
yr=int(input("Enter the year:"))
if yr%4==0:
    if yr%100==0:
        if yr%400==0:
            print("This is a leap year.")
        else:
            print("This is not a leap year.")
    else:
        print("This is a leap year.")
else:
    print("This is not a leap year.")




#SIMPLER FORM:
yr=int(input("Enter the year:"))
if (yr%4==0 and yr%400==0) or (yr%4==0 and yr%100!=0):
    print("This is a leap year.")
else:
    print("This is not a leap year.")

#yr%4==0 and yr%100!=0: This means that this is a leap year, but is not a
#century year.

#yr%4==0 and yr%400==0: A century year MUST be divisible by 400 to be a LY.
