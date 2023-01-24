scl=dict()
i=1
n=int(input("Enter the number of entries:"))
while i<=n:
  adm=input("Enter the admission number:")
  nm=input("Enter the student's name:")
  roll_no=int(input("Enter the roll no:"))
  total=int(input("Enter total score:"))
  if total>=450:
    grd='A'
  elif total>=350:
    grd='B'
  elif total>=350:
    grd='C'
  elif total>=250:
    grd='D'
  else:
    grd='E'
    
  b=(nm,roll_no,total,grd)
  scl[adm]=b
  i+=1
l=scl.keys()

for i in scl:
  print("\nAdmission Number",i,":")
  z=scl[i]
  print("Name\t","Roll Number\t","Total\t","Grade\t")
  for j in z:
    print(j,end='\t')
