while True:
    sel=int(input('''1- Sum of series
2- Prime palindrome numbers between 110 to 900
3- Exit
Select an option:'''))
    if sel==1:
        s=0
        n=int(input("Enter the number of terms:"))
        x=int(input("Enter the x term:"))
        y=int(input("Enter the y term:"))
        for i in range(1,n+1):
            fac=1
            for j in range(1,2*i+1):
                fac*=j
            s+=((x**i)*(y**(i+1)))/fac
        print("The sum of the series is:",s)
        
    elif sel==2:
        for i in range(111,900):
            a=str(i)
            if a==a[::-1]:
                count=0
                for j in range(1,i+1):
                    if i%j==0:
                        count+=1
                if count==2:
                    print(i)
    elif sel==3:
        print("Come back soon!")
        break
    
