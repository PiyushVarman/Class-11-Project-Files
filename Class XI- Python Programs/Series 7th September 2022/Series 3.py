n=int(input("Enter the n value:"))
a,b=65,1
for i in range(1,n):
    print(chr(a),b,"#",sep='')
    a+=2
    b+=2
