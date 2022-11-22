s1=int(input("Enter the mark of subject 1:"))
s2=int(input("Enter the mark of subject 2:"))
s3=int(input("Enter the mark of subject 3:"))
s4=int(input("Enter the mark of subject 4:"))
s5=int(input("Enter the mark of subject 5:"))
avg=(s1+s2+s3+s4+s5)/5
print("Your average is:",avg)

#Pass Parameters:
if avg<40:
    print("You have failed.")
else:
    print("You have passed.")

#Grade Parameters:
if avg>=90:
    print("Your grade is A.")
elif avg>=75:
    print("Your grade is B.")
elif avg>=40:
    print("Your grade is C.")
#Ignore D given in the question, as ma'am has said to take >40 as fail parameter.


