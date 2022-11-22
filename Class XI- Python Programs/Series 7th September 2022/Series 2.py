'''n=int(input("Enter the n value:"))
a=("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
for i in range(1,n+1):
    print(a[0:i])
'''
n=int(input("Enter the n value:"))
a=65
for i in range(1,n+1):#Number of lines
    for z in range(1,i):
        print(chr(a))
        a+=1
