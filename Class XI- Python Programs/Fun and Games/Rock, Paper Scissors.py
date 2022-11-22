w,cw=0,0
t='𝑹𝒐𝒄𝒌, 𝑷𝒂𝒑𝒆𝒓, 𝑺𝒄𝒊𝒔𝒔𝒐𝒓𝒔!'
print(t.center(99,'*'))
while True: #Infinite loop
    import random
    cpu=random.choice(['Rock','Paper','Scissors'])

    x=input("\nEnter Either Rock, Paper or Scissors (or q if you want to leave):").lower()

    #Removing invalid scenarios
    if x[0]!='r' and x[0]!='p' and x[0]!='s' and x!='q':
        print("Sorry, try once more.")
    #The win/loss can only be decided when a valid input has been provided by the user
    else:
        if x!='q':
            print("The computer chose",cpu,".")
        if x[0]=='r' and cpu=='Scissors':
            print("You won!")
            w+=1
        elif x[0]=='p' and cpu=='Rock':
            print("You won!")
            w+=1
        elif x[0]=='s' and cpu=='Paper':
            print("You won!")
            w+=1
        elif x[0]==cpu[0].lower():
            print("it's a tie! Equal points awarded.")
            cw+=1
            w+=1
        elif x[0]=='q':
            #Scorecard
            print("You won against the computer",w,"times.")
            print("The computer won",cw,"times!")
            #Status of the game
            if cw>w:
                print("\nOh no! The computer is champion! Better luck next time!")
            elif w>cw:
                print("\nWhat a fantastic game you have played! You're clearly champion!")
                print("Come back later!")
            else:
                print("\nPhew! What a closely contested game! It ends in a draw!\nCome back soon!")
            
            w,cw=0,0
            break
        else:
            print("Oh no! The computer won!")
            cw+=1
    
