n=int(input("Enter the number 'n':"))
nfac=1
for i in range(1,n+1):
    nfac=nfac*i
r=int(input("Enter the number 'r':"))
nrfac=1
for i in range(1,(n-r)+1):
    nrfac=nrfac*i
print(n,"P",r," is ",int(nfac/nrfac),sep='')
