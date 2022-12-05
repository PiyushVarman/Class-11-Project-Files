while True:
    sel=int(input('''1- Decimal to Binary Conversion
2- Binary to Decimal Conversion
3- Decimal to Octal Conversion
4- Exit
Enter your choice:'''))

    #Decimal to Binary 
    if sel==1:
        dnum=int(input("\nEnter the decimal number:"))
        bnum=[]
        i=0
        while dnum!=0:
            l_dig=dnum%2
            bnum.insert(i,l_dig)
            i+=1
            dnum=int(dnum/2)

        i-=1
        print("The equivalent binary value is:")
        while i>=0:
            print(end=str(bnum[i]))
            i-=1
        print("\n")
    


    #Binary to Decimal
    elif sel==2:
        bnum=int(input("\nEnter the binary number:"))
        dnum,mod,rem=[],0,0
        for i in range(len(str(bnum))):
            rem=bnum%10
            mod=bnum//10
            dnum.append(rem*(2**i))
            bnum=mod
        print("The equivalent decimal number is:",sum(dnum),"\n")


    #Decimal to Octal
    elif sel==3:
        dnum=int(input("\nEnter the decimal number:"))
        onum=[]
        i=0
        while dnum!=0:
            l_dig=dnum%8
            onum.insert(i,l_dig)
            i+=1
            dnum=int(dnum/8)

        i-=1
        print("The equivalent octal value is:")
        while i>=0:
            print(end=str(onum[i]))
            i-=1
        print("\n")
    
    elif sel==4:
        break
