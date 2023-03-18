n=input("Enter the name of the employee:")
sal=int(input("Enter "+n+"'s salary:"))
if sal>20000:
    bon=(20/100)*sal
elif sal>10000:
    bon=(18/100)*sal
else:
    bon=(16/100)*sal
print("Name of the employee:",n)
print("Salary:",sal)
print("Bonus:",bon)
print("Total salary:",sal+bon)
