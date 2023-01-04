a=eval(input("Enter the tuple:"))                                                
count,s=0,0
for i in range(len(a)):
    for j in range(len(a[i])):
        s+=a[i][j]
        count+=1
print("the average of the numbers within the nested tuple is",s/count)
print("The average of the average is",(s/count)/count)
