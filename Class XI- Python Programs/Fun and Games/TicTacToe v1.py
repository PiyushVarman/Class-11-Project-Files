import random
k=1
matrix=[]
for i in range(3):
    n=[]
    for j in range(3):
        n.append(k)
        k+=1
    matrix.append(n)

def matprint():
    for i in range(3):
        for j in range(3):
            print(matrix[i][j],end=' ')
        print()
matprint()
l=[1,2,3,4,5,6,7,8,9]
while True:
    play=[]
    while len(l)!=0:
        cpu=random.choice(l)
        a=int(input("\nEnter the index number here:"))
        if a in l:
            play.append(a)
            for i in range(3):
                for j in range(3):
                    if matrix[i][j]==a:
                        print("\nThe player has moved to",a,"position!")
                        matrix[i][j]='X'
                        l.remove(a)
                        matprint()

            

            for i in range(3):
                for j in range(3):
                    if matrix[i][j]==cpu:
                        print("\nThe CPU has moved to",cpu,"position!")
                        matrix[i][j]='O'
                        l.remove(cpu)
                        matprint()

            print(play)
        
            
        else:
            print("\nSorry, invalid number! Try again!")


    

        
    
