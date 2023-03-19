l=[]
n=int(input("Enter the number of tuples:"))
for i in range(n):
    l.append(eval(input("Enter the tuple:")))
l=tuple(l)
count=1
for i in l:
    print("Row number",count,":")
    print("Largest:",max(i))
    print("Smallest",min(i))
    print("Average:",sum(i)/len(i))
    print()
    
