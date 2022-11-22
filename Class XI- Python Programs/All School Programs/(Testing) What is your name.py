x=input("What is your name?")
print("All right then, I will remember you.")
z=input("Would you like to know your name? (y/n)")
if z=='y' or z=='Y':
    print("Your name is:",x)
    print("Have a great day!")

if z=='n' or z=='N':
    print("OK No worries.")
    
else:
    print("I'm sorry, I can't get you. Try restarting the program and try again.")
