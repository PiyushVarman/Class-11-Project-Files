input("Hello! Welcome to my chatbot! Hit enter to continue.")
print("For customer grievances, press 1. To talk to me, press 2.")
x=int(input("Enter Number from aforementioned code."))
if x==1:
    print("Oh! We apologize for the inconvenience.")
    print("For a return order, press 1. For a refund, press 2. For an exchange, press 3.")
    y=int(input("Enter number from the code."))

    if y==1:
        print("Absolutely! We will schedule your return today.")
    if y==2:
        print("Your refund is under processing right away!")
    if y==3:
        print("Your product will be exchanged today!")
    print("Thank you for shopping with us!")

if x==2:
    print("Hello and welcome to PCV Chatbot. I am PCV. I am the head of the chatbot division of Amazon India.")
    z=input("How do you do today?")
    print("That is wonderful to hear!")
    print("If you enjoyed our talk, please don't hesitate to rate us!")
    a=int(input("On a scale of 1-5, how was our conversation and experience?"))
    if a>5:
        print("That's invalid. Restart the program and try again!")        
    if a<3:
        print("Oh no! How can we improve?")
        b=input("Please give us your ideas!")
        print("All right! I will direct that to my senior departments! Thank you very much!")
    if a>=3 and a<=5:
        print("That's wonderful to hear! Thank you very much and have a great day!")
