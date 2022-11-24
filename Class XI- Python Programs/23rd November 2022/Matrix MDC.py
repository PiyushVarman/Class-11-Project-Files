m=int(input("Enter the number of rows:"))
n=int(input("Enter the number of columns:"))
matrix=[]
for i in range(m):
    temp=[]
    print("Row",i+1)
    for j in range(n):
        temp.append(int(input("Enter number "+str(j+1)+":")))
    matrix.append(temp)
print("The matrix is:")
for i in range(m):
    for j in range(n):
        print(matrix[i][j],end=' ')
    print()

while True:
    sel=int(input('''\n\nSelect a choice to:
1-Print the elements of the main diagonal
2-Print the elements of the secondary diagonal
3-Print the sum of the diagonal elements(main and secondary)
4-Print the elements of the lower triangle of main diagonal
5-Print the elements of the upper triangle of main diagonal
6-Print the elements of the border diagonal
7-Quit'''))

    if sel==1:
        print("\nThe elements of the main diagonal are:")
        a=0
        for i in range(m):
            for j in range(n):
                if i==j:
                    print(matrix[i][j],end='')
                    a+=matrix[i][j]
                else:
                    print(" ",end='')
            print()
                    

    if sel==2:
        print("\nThe elements of the secondary diagonal are:")
        b=0
        for i in range(m):
            for j in range(n):
                if i+j==(m-1):
                    print(matrix[i][j],end='')
                    b+=matrix[i][j]
                else:
                    print(" ",end='')
            print()
                    
    if sel==3:
        a=0
        for i in range(m):
            for j in range(n):
                if i==j:
                    a+=matrix[i][j]
        b=0
        for i in range(m):
            for j in range(n):
                if i+j==(m-1):
                    b+=matrix[i][j]
        print("\nThe sum of the main diagonal elements are:",a)
        print("The sum of the secondary diagonal elements are:",b)

    if sel==4:
        print("\nThe elements of the lower triangle of the main diagonal are:")
        for i in range(m):
            for j in range(n):
                if (i>=j):
                    print(matrix[i][j],end='')
                else:
                    print(" ",end='')
            print()
                

    if sel==5:
        print("\nThe elements of the upper triangle of the main diagonal are:")
        for i in range(m):
            for j in range(n):
                if (i<=j):
                    print(matrix[i][j],end='')
                else:
                    print(" ",end='')
            print()

    if sel==6:
        print("\nThe elements of the border diagonal are:")
        for i in range(m):
            for j in range(n):
                if j==0 or j==n-1 or i==0 or i==m-1:
                    print(matrix[i][j],end='')
                else:
                    print(" ",end='')
            print()
                
    if sel==7:
        print("Come back later!")
        break
