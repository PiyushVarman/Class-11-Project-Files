#There is a mistake in the question. the third line should end with 6
for i in range(5,0,-1):
    l=[]
    for j in range(i,0,-1):
        l.append(j)
        print(j,end="")
    print("-",sum(l),sep="")
    
    
