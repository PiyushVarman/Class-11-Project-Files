l=[]
for i in range(4):
    temp=[]
    for j in range(4):
        temp.append(int(input("Enter the number:")))
    l.append(temp)
md,sd=l[0][0],l[0][3]

for i in range(4):
    for j in range(4):
        print(l[i][j],end=" ")
    print()
for i in range(4):
    for j in range(4):
        if i==j:
            if l[i][j]>md:
                md=l[i][j]
        if i+j==3:
            if l[i][j]>sd:
                sd=l[i][j]
print("The maximum among main diagonal is",md)
print("The maximum among secondary diagonal is",sd)
print("The mean of the elements are:",(sd+md)/2)
