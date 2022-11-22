s=input("Enter the string:")
s=s.lower()
if s[0:len(s)]==s[::-1]:
    print("This is a palidrome.")
else:
    print("This is not a palindrome.")

