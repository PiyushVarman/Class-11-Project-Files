m=int(input("Enter the number of rows and columns:"))
mat=[]
for i in range(m):
    tup=eval(input())
    temp=[i for i in tup]
    mat.append(temp)
print(mat)
