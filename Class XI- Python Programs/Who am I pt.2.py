whoami=input("What is your name?")
nname=input("What is your nickname?")
x=input("Do you want to know your name and nickname?")
if x=='Y' or x=='y' or x=='Yes' or x=='yes':
    print("Your name is",whoami,"and your nickname is",nname)
elif x=='N' or x=='n' or x=='No' or x=='no':
    print("All right, see you!")
else:
    print("Sorry! That does not work here. Hit F5 to try again!")
