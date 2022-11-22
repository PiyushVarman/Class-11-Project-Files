s1=float(input("Enter the first side:"))
s2=float(input("Enter the second side:"))
s3=float(input("Enter the third side:"))

if (s1+s2>s3) and (s2+s3>s1) and (s3+s1>s2):
    if s1==s2==s3:
        print("This is an equilateral triangle.")
    elif (s1==s2) or (s2==s3) or (s3==s1):
        print("This is an isosceles triangle.")
    elif (s1!=s2!=s3):
        print("This is a scalene Triangle.")
else:
    print("This triangle is not possible.")
        
