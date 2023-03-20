import random
lottery={}
l=[]
while True:
    ticket_no=int(input("Enter the ticket number:"))
    l.append(ticket_no)
    z={}
    z["Name"]=input("Enter the ticket holder's name:")
    z["Address"]=input("Enter the ticket holder's address:")
    lottery[ticket_no]=z
    x=input("Do you wish to continue? (Y/N)").lower()
    if x[0]!="y":
        break
print(lottery)
print("Winners:")
for i in range(2):
    x=random.choice(l)
    l.remove(x)
    print("Ticket number:",x)
    print("Name:",lottery[x]["Name"])
    print("Address:",lottery[x]["Address"])
    print()
