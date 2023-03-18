l=[]
for i in range(4):
    t=eval(input("Enter the tuple:"))
    l.append(t)
en,on=0,0
print()
for i in range(4):
    for j in range(4):
        if i==0 or i==3 or j==0 or j==3:
            print(l[i][j],end=" ")
            if l[i][j]%2==0:
                en+=1
            else:
                on+=1
        else:
            print(" ",end=" ")
    print()
print("\nThe number of odd numbers are:",on)
print("The number of even numbers are:",en)
