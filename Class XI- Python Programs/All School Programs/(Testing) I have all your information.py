x=input("What is your name?")
y=input("Which school are you from?")
z=int(input("Which year were you born in?"))

if z<=2000:
    print("Sorry too old to use this.")
if z>2022:
    print("Come back when you are old enough to use this/ when you are born.")
else:
    print("You are",x,",you belong to",y,"school, and, you are approximately",2022-z,"years old.")
    print("Thank you for using my program!")
