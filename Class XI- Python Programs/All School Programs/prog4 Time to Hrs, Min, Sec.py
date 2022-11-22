x=int(input("Enter Time in seconds:"))
hrs=x//3600
min_=(x%3600)//60
sec= x%60
print("H:",hrs,"M:",min_,"S:",sec)

H=int(input("Enter hours:"))
M=int(input("Enter minutes:"))
S=int(input("Enter seconds:"))
print(H,M,S ,sep=':')
print("The number of seconds are:",H*3600+M*60+S)
