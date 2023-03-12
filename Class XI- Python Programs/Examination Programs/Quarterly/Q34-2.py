n=int(input("Enter the number of students:"))
for i in range(n):
    rn=int(input("Enter the roll number:"))
    na=input("Enter the name:")
    st=input("Enter the stream:").lower()
    cl=int(input("Enter the class:"))
    if cl==11:
        if st[0]=="s":
            print(65000)
        elif st[0]=='c':
            print(50000)
        else:
            print("Wrong stream entered.")
    elif cl==12:
        if st[0]=="s":
            print(74000)
        elif st[0]=='c':
            print(55000)
        else:
            print("Wrong stream entered.")
    else:
        print("Wrong class entered.")
