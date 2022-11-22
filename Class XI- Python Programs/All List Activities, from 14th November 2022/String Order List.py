n=int(input("Enter the number of terms:"))
l=[]
for i in range(n):
    l.append(input("Enter String "+str(i+1)+":"))
for i in range(len(l)):
    for j in range(len(l)):
        a,b=l[i].lower(),l[j].lower()
        a,b=a.lower(),b.lower()
        w=0
        a,b=a[w],b[w]
        if ord(a)<ord(b):
            l[i],l[j]=l[j],l[i]
        elif ord(a)<ord(b):
            while ord(a)==ord(b):
                w+=1
                if ord(a)<ord(b):
                    l[i],l[j]=l[j],l[i]
                    break
            w=0
print("The list is",l)
            
        
        
            


