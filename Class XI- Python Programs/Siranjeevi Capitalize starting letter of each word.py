#Sample 1
st=input("enter string:")
s = ''
r = st.split()
print(r)
for i in range(0,len(r)):
    print(r[i].strip(r[i][0]))
    s += " " + r[i][0].upper() + r[i].strip(r[i][0])    
print(s)

'''


#Sample 2
n = input("The Text you want to capitalize: ").lower()
a = chr(ord(n[0])-32)
for i in range (1,len(n)):
    a+=n[i]

# To capitalize the first letter of the string

i = 0

while i < len(n):
    if a[i] != " ":
        print(a[i], end ="")
        i+=1
    else:
        print(" "+chr(ord(a[i+1])-32), end = "")
        i+=2
'''
