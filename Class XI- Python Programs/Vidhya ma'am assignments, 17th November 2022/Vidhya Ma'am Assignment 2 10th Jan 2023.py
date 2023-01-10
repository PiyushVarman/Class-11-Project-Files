n=int(input("Enter the number of rows:"))
k=0
for i in range(n+1):
    for j in range(i+1):
        print(k*j,end=' ')
        
    print()
    k+=1
    
