n=int(input("Enter the number of pairs:"))
pairs=[]
for i in range(n):
    print("Pair number",i+1)
    temp=[]
    for j in range(2):
        temp.append(input("Enter element "+str(j+1)+":"))
    pairs.append(tuple(temp))

for i in range(len(pairs)):
    if i+1<len(pairs)-1:
        if pairs[i][0]>pairs[i+1][0]:
            pairs[i],pairs[i+1]=pairs[i+1],pairs[i]
print(tuple(pairs))
