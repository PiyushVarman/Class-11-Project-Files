l=eval(input("Enter the list of names:"))
s=0
for i in range(len(l)):
    if len(l[i])%2!=0:
        s+=len(l[i])
        if len(l[i])%5==0:
            l[i]=l[i][-1]+l[i][1:len(l[i])-1]+l[i][0]
print(l)
                
    
