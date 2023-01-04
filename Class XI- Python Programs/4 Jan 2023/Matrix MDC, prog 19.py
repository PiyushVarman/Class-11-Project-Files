m=int(input("Enter the number of rows and columns:"))
matrix=[]
for i in range(m):
    print("Row number",i+1)
    temp=[]
    for j in range(m):
        temp.append(int(input("Enter number "+str(j+1)+":")))
    matrix.append(temp)

for i in range(m):
    for j in range(m):
        print(matrix[i][j],end=' ')
    print()

while True:
    sel=int(input('''1- To print the sum of the diagonals
2- To print the upper triangular region of the main diagonal
3- To print the lower triangular region of the secondary diagonal
4- To print the prime palindromic numbers within the matrix
5- Exit
Enter your desired option: '''))
    print()
    #Printing the sum of the diagonals
    if sel==1:
        s=0
        for i in range(m):
            for j in range(m):
                if i==j:
                    s+=matrix[i][j]
                elif i+j==(m-1) and i!=j:
                    s+=matrix[i][j]

        print("The sum of the 2 diagonals of the matrix are:",s)
        print()

    if sel==2:
        for i in range(m):
            for j in range(m):
                if i<=j:
                    print(matrix[i][j],end=' ')
                else:
                    print(' ',end=' ')
            print()

        print()

    if sel==3:
        for i in range(m):
            for j in range(m):
                if (i+j)>=m-1:
                    print(matrix[i][j],end=' ')
                else:
                    print(' ',end=' ')
            print()
        print()

    if sel==4:
        pp=[]
        for i in range(m):
            for j in range(m):
                count=0
                for k in range(1,matrix[i][j]+1):
                    if matrix[i][j]%k==0:
                        count+=1
                if count==2:
                    b=str(matrix[i][j])
                    if b==b[::-1]:
                        pp.append(matrix[i][j])

        print("The palindromic prime numbers within the matrix are:",end=' ')
        for i in range(len(pp)):
            print(pp[i],end=',')
        print('\n\n')

    if sel==5:
        print("Come back soon!")
        break
            
            
