yr=int(input("Enter the year you want to check for:"))
if yr%4==0:
    if yr%100==0:
        if yr%400==0:
            print(yr,"is a leap year.")
        else:
            print(yr,"is not a leap year.")
    else:
        print(yr,"is a leap year.")
else:
    print(yr,"is not a leap year.")
