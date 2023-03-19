n=int(input("Enter the number of lines:"))
j=1
for i in range(1,2*n,2):
    if j%2!=0:
        for k in range(1,i+1,2):
            print(k,end=" ")
        j+=1
    else:
        for k in range(i,0,-2):
            print(k,end=" ")
        j+=1
    print()
    
