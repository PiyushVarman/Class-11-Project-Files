n=int(input("Enter the number of strings:"))
l,v=[],[]
for i in range(n):
    l.append(input("Enter string "+str(i+1)+":").lower())
for i in l:
    count=0
    for j in range(len(i)):
        if i[j] in 'aeiou':
            count+=1
    v.append(count)
v.sort()
for i in l:
    count=0
    for j in range(len(i)):
        if i[j] in "aeiou":
            count+=1
        if count==v[-1]:
            print(i,"is the string with maximum vowels with",count,"vowels.")
            break
