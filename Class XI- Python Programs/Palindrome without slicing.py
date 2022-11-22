st=input("Enter the string:")
a=st.lower()
status=0
for i in range(len(st)):
    if a[-(i+1)]==a[i]:
        status+=1
    else:
        print(st,"is not a palindrome.")
        break
    
if status==len(st):
    print(st,"is a palindrome.")
