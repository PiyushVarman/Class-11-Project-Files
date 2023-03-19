count=0
n=input("Enter the string:")
for i in n:
    if i.isdigit() or i.isalpha():
        continue
    else:
        count+=1
print("The number of special characters is",count)
