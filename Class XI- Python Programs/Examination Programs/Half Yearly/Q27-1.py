matrix=[]
for i in range(3):
    print("Row Number",i+1)
    temp=[]
    for j in range(3):
        temp.append(int(input("Enter number "+str(j+1)+":")))
    matrix.append(temp)
s=0
print()
for i in range(3):
    for j in range(3):
        if i>=j:
            print(matrix[i][j],end=" ")
            s+=matrix[i][j]
        else:
            print(" ",end=" ")
    print()
print("\nThe sum of lower triangle numbers =",s)
