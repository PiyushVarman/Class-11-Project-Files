d={}
n=int(input("Enter the number of teachers:"))
for i in range(n):
    l=[]
    tn=input("Enter the teacher's name:")
    l.append(input("Enter the subject handled:").lower())
    l.append(input("Enter the date of join:").lower())
    l.append(input("Enter the gender:").lower())
    l.append(int(input("Enter the number of periods:")))
    l.append(int(input("Enter salary:")))
    d[tn]=l
print(d)
for i in d.keys():
    if d[i][0]=="physics" and int(d[i][1][-2::])<10:
        d[i][3]-=2
    
print(d)
        
