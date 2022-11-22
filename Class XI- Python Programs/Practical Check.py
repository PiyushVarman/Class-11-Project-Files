'''p=int(input("Enter the principal amount:"))
r=int(input("Enter the rate of interest:"))
t=int(input("Enter the time period:"))
SI=(p*r*t)/100
A=SI+p
print("The Simple Interest is Rs.",SI)
print("The Amount is Rs.",A)

'''
'''
t=int(input("Enter the time in seconds."))
hr=t//3600
min_=(t%3600)//60
sec=t%60
print(hr,min_,sec,sep=':')

h=int(input("Enter the hours:"))
m=int(input("Enter the minutes:"))
s=int(input("Enter the seconds:"))
print(h,m,s,sep=':')
print("The number of seconds is:",(h*3600)+(m*60)+s)
'''
'''
name=input("Enter your name:")
s1=int(input("Enter the marks of the first subject:"))
s2=int(input("Enter the marks of the second subject:"))
s3=int(input("Enter the marks of the third subject:"))
s4=int(input("Enter the marks of the fourth subject:"))
s5=int(input("Enter the marks of the fifth subject:"))
avg=(s1+s2+s3+s4+s5)/5

print('''#Your name is:''',name,'''
#Your average is:''',avg,end='\n\n')
'''
if avg<40:
    print("You have failed.")
else:
    print("You have passed.")
    if avg>=90:
        print("Your grade is A.")
    elif avg>=75:
        print("Your grade is B.")
    elif avg>=40:
        print("Your grade is C.")
'''
'''
temp1=float(input("Enter the temperature in Celsius:"))
print(temp1,"°C is",((9/5)*temp1)+32,"°F")
temp2=float(input("Enter the temperature in Fahrenheit:"))
print(temp2,"°F is",(5/9)*(temp2-32),"°C")
'''
'''
y=int(input("Enter the year:"))
if y%4==0:
    if y%100==0:
        if y%400==0:
            print(y,"is a leap year.")
        else:
            print(y,"is not a leap year.")
    else:
        print(y,"is a leap year.")
else:
    print(y,"is not a leap year.")
'''
'''
a=int(input("Enter the coefficient of x²:"))
b=int(input("Enter the coefficient of x:"))
c=int(input("Enter the constant value:"))
d=(b**2)-(4*a*c)
s1,s2=(-b+(d**0.5))/(2*a),(-b-(d**0.5))/(2*a)
if d<0:
    print("There are no real roots for this equation.")
if d==0:
    print("There are 2 equal roots for this equation, they are",s1)
if d>0:
    print("There are 2 real roots for this equation, they are",s1,"and",s2)
'''
'''
sel=int(input('''#1-Area of a Circle
#2-Perimeter of a circle
#3-Exit\n
#Enter your desired option.'''))
'''
if sel==1:
    r=int(input("Enter the radius of the circle in cm:"))
    print("The area of the circle is:",3.14*r*r,"cm².")
elif sel==2:
    r=int(input("Enter the radius of the circle in cm:"))
    print("The perimeter of the circle is:",2*3.14*r,"cm.")
elif sel==3:
    print("Come back later.")
'''
'''
sel=int(input('''#1-Sum of n terms
#2-Multiplication table of n with m multiples
#3-Exit\n
#Enter your desired option.
'''))
if sel==1:
    n=int(input("Enter the n value:"))
    s=0
    for i in range(1,n+1):
        s+=i
    print(s,"is the sum of",n,"terms.")
elif sel==2:
    n=int(input("Enter the n value:"))
    m=int(input("Enter the m value:"))
    for i in range(1,m+1):
        print(n,"times",m,"is",n*i)
elif sel==3:
    print("Come back later.")
'''
'''
n=int(input("Enter the number:"))
a,b=-1,1
for i in range(1,n+1):
    c=a+b
    a,b=b,c
    print(c,end=',')
print("is the fibonacci series for n=",n,sep='')
'''
'''
l=int(input("Enter the lower limit:"))
u=int(input("Enter the upper limit:"))
for i in range(l,u+1):
    count=0
    for z in range(1,i+1):
        if i%z==0:
            count+=1
    if count==2:
        print(i,end=',')
print("are prime numbers in the range",l,"to",u)
