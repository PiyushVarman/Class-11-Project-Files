n=int(input("Enter the number:"))
print("Fibo is:",end=' ')
a,b=-1,1
for i in range(n):
    c=a+b
    print(c,end=',')
    a,b=b,c
