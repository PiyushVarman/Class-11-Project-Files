l=[]
while True:
    n=int(input("Enter the number:"))
    if n!=-1:
        l.append(n)
    else:
        break
print("Maximum =",max(l))
print("Minimum =",min(l))
print("Mean =",sum(l)/len(l))
