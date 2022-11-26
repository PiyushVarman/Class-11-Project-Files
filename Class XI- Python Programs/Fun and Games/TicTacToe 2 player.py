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
    comp=[]
    while len(l)!=0:
        a=int(input("\nPlayer 1, enter the index number here:"))
        if a in l:
            play.append(a)
            for i in range(3):
                for j in range(3):
                    if matrix[i][j]==a:
                        print("\nPlayer 1 has moved to position ",a,"!",sep='')
                        matrix[i][j]='X'
                        l.remove(a)
                        matprint()
            
            
            if 1 in play and 2 in play and 3 in play:
                print("Player 1 wins!")
                break
            elif 1 in play and 4 in play and 7 in play:
                print("Player 1 wins!")
                break
            elif 7 in play and 8 in play and 9 in play:
                print("Player 1 wins!")
                break
            elif 3 in play and 6 in play and 9 in play:
                print("Player 1 wins!")
                break
            elif 4 in play and 5 in play and 6 in play:
                print("Player 1 wins!")
                break
            elif 2 in play and 5 in play and 8 in play:
                print("Player 1 wins!")
                break
            elif 1 in play and 5 in play and 9 in play:
                print("Player 1 wins!")
                break
            elif 3 in play and 5 in play and 7 in play:
                print("Player 1 wins!")
                break

            if len(l)!=0:
                cpu=int(input("\nPlayer 2, enter the index number here:"))
                

            comp.append(cpu)
            
            for i in range(3):
                for j in range(3):
                    if matrix[i][j]==cpu:
                        print("\nPlayer 2 has moved to position ",cpu,"!",sep='')
                        matrix[i][j]='O'
                        l.remove(cpu)
                        matprint()

            if 1 in comp and 2 in comp and 3 in comp:
                print("Oh no! The computer wins!")
                break
            elif 1 in comp and 4 in comp and 7 in comp:
                print("Player 2 wins!")
                break
            elif 7 in comp and 8 in comp and 9 in comp:
                print("Player 2 wins!")
                break
            elif 3 in comp and 6 in comp and 9 in comp:
                print("Player 2 wins!")
                break
            elif 4 in comp and 5 in comp and 6 in comp:
                print("Player 2 wins!")
                break
            elif 2 in comp and 5 in comp and 8 in comp:
                print("Player 2 wins!")
                break
            elif 1 in comp and 5 in comp and 9 in comp:
                print("Player 2 wins!")
                break
            elif 3 in comp and 5 in comp and 7 in comp:
                print("Player 2 wins!")
                break
            elif len(l)==0:
                print("What a closely contested game! It ends in a tie!")

        
            
        else:
            print("\nSorry, invalid number! Try again!")
    
    break
