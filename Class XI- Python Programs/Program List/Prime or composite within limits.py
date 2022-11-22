l=int(input("Enter the lower limit:"))
u=int(input("Enter the upper limit:"))
for i in range(l,u+1):
    count=0
    for z in range(1,i+1):
        if i%z==0:
            count+=1
    if count==2:
        print(i,end=',')
print("are prime numbers in the range",l,"-",u)
    
