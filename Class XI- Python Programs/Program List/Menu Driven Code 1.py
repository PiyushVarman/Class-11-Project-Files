sel=int(input('''\n1-Area of a circle  
\n2-Perimeter of a circle
\n3-Exit
\nEnter Your desired option.''')) #Sel=Selector.

#Area of Circle
if sel==1:
    r=float(input("Enter the radius of the circle in cm."))
    print("The area of the circle with radius",r,"cm is",(3.14*r*r))
#Perimeter of circle
elif sel==2:
    r=float(input("Enter the radius of the circle in cm."))
    print("The perimeter of the circle with radius",r,"cm is",(2*3.14*r))
#ExIt, ExIt NoW:    
elif sel==3:
    print("Come back later!")
