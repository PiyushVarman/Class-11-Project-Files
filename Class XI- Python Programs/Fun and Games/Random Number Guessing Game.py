import random
a=random.randint(1,10)
st=1
while True:
    
    x=int(input("\nCan you guess the number I am thinking of from 1 to 10?"))
    if x==a:
        print("\nYES! I was thinking about the number",a,".")
        if st==1:
            print("You guessed the number in your very first try! Amazing!")
        else:
            print("\nYou guessed the number in",st,"tries.")
        input("\nClick enter to terminate the program.")
        break
    elif x<a:
        st+=1
        print("No, the number is higher than",x,".")
        
    elif x>a:
        st+=1
        print("No, the number is lower than",x,".")
