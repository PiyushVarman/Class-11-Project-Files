x=int(input("On a scale of 1 to 10, how do you feel today, with 10 being the highest?"))
if x<=3:
    input("Why? What's wrong?")
    print("I feel you! You will be better soon!")
elif x>3 and x<=5:
    print("Pretty average, eh?")
elif x>5 and x<8:
    print("All right! You can feel better!")
elif x>=8 and x<=10:
    print("AYY! Have a great day!")
