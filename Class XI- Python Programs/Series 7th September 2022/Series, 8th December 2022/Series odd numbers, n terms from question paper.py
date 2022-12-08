n=int(input("Enter the number of terms:"))
s,d=0,0
for i in range(1,n+2,2):
    s+=i
    d+=s
print("The sum of all the terms is:",d)
    
