n=int(input("Enter the number of terms:"))
l,start,end,st=[],0,(n-1),0
for i in range(n):
    l.append(int(input("Enter number "+str(i+1)+":")))
l.sort()
data=int(input("Enter number to be searched:"))
while start<=end:
    mid=(start+end)//2
    if (l[mid]==data):
        st=1
        break
    elif (l[mid]>data):
        last=mid-1
    else:
        start=mid+1
if st==1:
    print(data,"is found at the",mid+1,"position.")
else:
    print(data,"is not found in the list.")
