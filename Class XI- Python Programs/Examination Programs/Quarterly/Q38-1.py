while True:
    sel=int(input('''1- Number of factors of a number
2- Sum of first "n" even numbers
3- Exit
Select an option'''))
    if sel==1:
        n=int(input("Enter the number to be checked for:"))
        count=0
        for j in range(1,n+1):
            if n%j==0:
                count+=1
        print("The number of factors of",n,"are",count)
    
    elif sel==2:
        n=int(input("Enter the number:"))
        s=0
        for i in range(0,n+1,2):
            s+=i
        print("The sum of all even numbers till",n,"is",s)
    elif sel==3:
        print("See you later!")
        break
            
        
