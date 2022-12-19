import math
print("Welcome to my area of a triangle calculator!")
a=int(input("Enter the length of the first side:")) #Side1
b=int(input("Enter the length of the second side:"))#Side2
c=int(input("Enter the length of the third side:")) #Side3
s=(a+b+c)/2 #Semiperimeter
area=math.sqrt(s*(s-a)*(s-b)*(s-c)) #Area
print("\nThe semiperimeter of this triangle is:",s)
print("The area of the triangle with sides of lengths",a,",",b,"and",c,"is",'%.2f'%area,"Square units.")

