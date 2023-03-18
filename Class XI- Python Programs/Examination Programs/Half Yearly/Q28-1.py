s="@"
for i in range(0,6):
    if i==0 or i%2!=0:
        print(1*(10**i),end="")
        if s.isalpha():
            print(s,end="")
        print()
        s=chr(ord(s)+1)
