import random
print('''RULES:
1. You can choose a number between 0 and 10 at any given time
2. 5 wickets, 30 balls per innings.
3. All the best!''')
number=[0,1,2,3,4,5,6,7,8,9,10]
player=input("What is your name?")
n=input("All right, "+player+"! It's time for the toss! Odd or Even? (O/E)").lower()
if n in'oe':
    toss=int(input("\nEnter a number between from 0 to 10:"))
    cpu=random.choice(number)
    if (n[0]=='e' and (cpu+toss)%2==0) or (n[0]=='o' and (cpu+toss)%2!=0):
        print("\nYou won!")
        n=int(input("If you would like to bat, click 1. If you would like to bowl, click 2."))
        
    else:
        print("You lost!")
        cpu=random.choice([1,2])
        if cpu==1:
            print("The computer would like to bat first!")
        else:
            print("The computer would like to bowl first!")
else:
    print("Whoops! It seems you have input an invalid character. Restart the program and try again!")
    quit()

cpuwicket=5
balls=30
if cpu==1 or n==2: #Player to bowl first, CPU bat first.
    cpuscore=0
    print("The computer walks onto the pitch! It's game on, as can be seen in their game faces...")
    while cpuwicket>0 and balls>0:
        cpu=random.choice(number)
        play=int(input("\nEnter a number between from 0 to 10:"))
        if play in number:
            if play==cpu:
                cpuwicket-=1
                balls-=1
                print("\nThe computer chose",cpu)
                print("HOW'S THATTTT??? You have taken a wicket! The CPU has",cpuwicket,"wickets remaining!")
            else:
                balls-=1
                print("\nThe computer chose",cpu)
                cpuscore+=cpu
            print("The computer has scored",cpuscore,"runs.")
            if balls%6==0:
                print("\nThat's the end of the over!",balls,"balls remain!")
        else:
            print("That's invalid!")
    playtarget=cpuscore+1
    if cpuwicket==0:
        print("The computer is all out! They have scored",cpuscore,"runs. Your target is",playtarget,".")
    else:
        print("That's the end of the innings! The computer has scored",cpuscore,"runs. Your target is",playtarget,".")


    print(player,"walks on to the pitch... oh-so-hoping that they will win!")
    playscore,balls,playwicket=0,30,5
    while playtarget>0 and playwicket>0 and balls>0:
        cpu=random.choice(number)
        play=int(input("\nEnter a number between from 0 to 10:"))
        if play in number:
            if play==cpu:
                playwicket-=1
                balls-=1
                print("\nThe computer chose",cpu)
                print("Oh no! The computer has taken a wicket! You have",playwicket,"wickets remaining!")
            else:
                balls-=1
                print("\nThe computer chose",cpu)
                playscore+=play
                playtarget-=play
            print("You have scored",playscore,"runs.")
            if balls%6==0 and balls!=0:
                print("\nThat's the end of the over!",balls,"balls remain!")
        else:
            print("That's invalid!")
    if playtarget<=0:
        print("You have won the game! You had",balls,"remaining.")
    elif playtarget>0:
        print("Oh no! The computer won this game! You lost this game by",playtarget-1,"runs.")

if cpu==2 or n==1: #CPU to bowl first, player to bat first
    print(player,"walks on to the pitch... The game is currently in the batter's hand...")
    playscore,balls,playwicket=0,30,5
    while playwicket>0 and balls>0:
        cpu=random.choice(number)
        play=int(input("\nEnter a number between from 0 to 10:"))
        if play in number:
            if play==cpu:
                playwicket-=1
                balls-=1
                print("\nThe computer chose",cpu)
                print("Oh no! The computer has taken a wicket! You have",playwicket,"wickets remaining!")
            else:
                balls-=1
                print("\nThe computer chose",cpu)
                playscore+=play
                cputarget=playscore+1
            print("You have scored",playscore,"runs.")
            if balls%6==0 and balls!=0:
                print("\nThat's the end of the over!",balls,"balls remain!")
        else:
            print("That's invalid!")
    print("That's the end of the innings!\nYou have scored",playscore,"runs. The computer will have to chase down",cputarget,"runs !")
        

    print("The computer walks onto the pitch! Can they win this game? Only the span of 30 balls will tell...")
    balls=30
    cpuscore=0
    while cpuwicket>0 and balls>0 and cputarget>0:
        cpu=random.choice(number)
        play=int(input("\nEnter a number between from 0 to 10:"))
        if play in number:
            if play==cpu:
                cpuwicket-=1
                balls-=1
                print("\nThe computer chose",cpu)
                print("HOW'S THATTTT??? You have taken a wicket! The CPU has",cpuwicket,"wickets remaining!")
            else:
                balls-=1
                print("\nThe computer chose",cpu)
                cpuscore+=cpu
                cputarget-=cpu
            print("The computer has scored",cpuscore,"runs.")
            if balls%6==0 and balls>0:
                print("\nThat's the end of the over!",balls,"balls remain!")
        else:
            print("That's invalid!")
            
    if cputarget>0:
        print("YOU HAVE WON! You win this game by",cputarget-1,"runs! Congratulations!")
    elif cpuwicket==0 and cputarget>0:
        print("The computer is all out!")
        print("YOU HAVE WON! You win this game by",cputarget-1,"runs! Congratulations!")
    elif cputarget==0 or cputarget<0:
        print("Oh no! The computer wins this game with",cpuwicket,"wickets in hand.")
