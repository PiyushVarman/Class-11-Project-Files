l=[]
print("Please note that the details you want to check for occurances are case sensitive.")
n=int(input("Enter the number of details you want to give me:"))

for i in range(n):
    enter=input("Enter detail number "+str(i+1)+":")
    l.append(enter)
for j in range(len(l)):
    count=0
    for k in range(len(l)):
        if l[j]==l[k]:
            count+=1

    print(l[j],"occurs",count,"time(s).")
