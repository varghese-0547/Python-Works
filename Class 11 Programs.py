'''
n=int(input("Enter a number : "))
f=[]
i=1
while i<n:
    if n%i==0:
        f.append(i)
    i+=1
print('While loop :',f)
f.clear()



for i in range(1,n):
    if n%i ==0:
        f.append(i)
print('For loop :',f)
'''




#Prgm to check the character is alphabet or not
'''
_=input("enter an alphabet : ")
#The line under is code to know ascii value of a character
print("The ascii value of", _,"is",ord(_))
if _>='A' and _<='Z' :
    print("It's corresponding small case is",chr(ord(_)+32),"and it's ascii value is",ord(_)+32)

elif _>='a' and _<='z':
    print("It's corresponding upper casse is",chr(ord(_)-32),"and it's ascii value is",ord(_)-32)

else :
    print("It's not a valid alphabet")

'''

'''
_=input("enter an alphabet : ")
if _.isalpha():
    if _.isupper():
        print("It's corresponding small case is",_.lower())
    else :
        print("It's corresponding upper casse is",_.upper())
'''


# Prgm to check discriminant
'''
a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))
c=int(input("Enter the third number : "))
if a!=0 :
    d=b**2-(4*a*c)
    if d>0 or (a<0 or c<0):
        r1=(-b+d**0.5)/(2*a)
        r2=(-b-d**0.5)/(2*a)
        print("The equation has real and distinct roots\nAnd the roots are ",r1,"and",r2)
    elif d==0 :
        r=b/(2*a)
        print("The equation has real and equal roots")
    else :
        print("The equation has no real roots or it has an imaginary root")
else :
    print("It's not a quadratic polynomial")
'''




#Prgm to find odd or even
'''
n=int(input("Enter a number : "))
if n%2 == 0:
    print("The number is even and it's square is ",n**2)
else :
    print("The number is odd and it's qube is ",n**3)
'''




#Prgm to find annual salary
'''
BP=int(input("Enter your basic pay per month : "))
DA=BP*(64/100)
TA=BP*(25/100)
HRA=BP*(15.5/100)
PR=BP*(12.5/100)
NS=(DA+TA+HRA)-PR
print("Your net salary per month is Rs.",NS)
PA=NS*12
if PA>=500000 :
    IT=PA*12.8/100
    print("You should pay Rs.",IT,"as income tax annually.")
'''




#Prgm to check nationality
'''
x=input("Enter your nationality : ")
if x== 'Indian' or x=='INDIAN' or x=='indian' :
    print("Nationality ocnfirmed")
else :
    print("Sorry, you are not an Indian")
'''


#prgm to find greatest of three no.s

'''
a=float(input("Enter a number"))
b=float(input("Enter another number"))
c=float(input("Enter another number"))
if a>b and a>c :
    print(a,"is greater")
elif b>a and b>c :
    print(b,"is greater")
elif c>a and c>b :
    print(c,"is greater")
else :
    print(a)
'''



#Calculate commission based on sales

'''
s=int(input("Enter sales : "))
if s>50000 :
    c=s*(10/100)
    print("C = ",c)
elif s>40000 :
    c=s*(8/100)
    print("C = ",c)
elif s>30000 :
    c=s*(5/100)
    print("C = ",c)
else :
    print("C = 0")
'''

#Prgm to check whether the character is alphabet, digit, space


'''
ch=input("Enter a character")
if ch>='a' and ch<='z' or ch>='A' and ch<='Z':
    _=[a,e,i,o,u,A,E,I,O,U]
    if ch in _ :
        print("It is a vowel")
    else :
        print("It's a consonant")
elif ch>='0' and ch<='9':
    print("It's a digit")
elif ch==' ':
    print("Space")
'''



#Prgm to calculate BMI 


'''
W=float(input("Enter your wiaght in kilogram"))
H=float(input("Enter your height in meter"))
BMI=W/(H**2)
if BMI<18.5:
    print("Your BMI is",BMI,"\nCategory : Underweight")
elif 18.5 <= BMI < 24.9:
    print("Your BMI is",BMI,"\nCategory : Normal")
elif 24.9 <= BMI < 30:
    print("Your BMI is",BMI,"\nCategory : Overweight")
elif BMI > 30:
    print("Your BMI is",BMI,"\nCategory : Obesity")
'''





# Prgm to find average


'''
i=0
s=0
n=int(input("Enter the limit : "))
while i<n:
    a=int(input("Enter the number : "))
    s+=a
    i+=1
print("Sum is =",s)
print("Average is =",s/n)

'''



#Read a number and find the factors




'''
a=int(input("Enter a number : "))
i=1
l=[]
while i<=a :
    
    if a%i==0:
        print(i,"is a factor")
        l.append(i)
    i+=1
print("Factors of",a,"is\n",l)

'''



#sum of n nos ending with 10



'''
n=int(input("Enter the limit : "))
i=0
s=0
while i<n :
    a=int(input("Enter a number : "))
    if a%10==0:
        s+=a
    i+=1
print (s)

'''


#Prgm to check the occurence of the number 50

'''
c=0
n=int(input("Enter the limit : "))
while n :
    a=float(input("Enter a number :"))
    if a==50:
        c+=1
    n-=0
print(c)
'''



#Prgm to find the factors of n numbers



'''
n=int(input("Enter a number : "))
i=1
l=[]
while i<=n:
    if n%i==0:
        print(i,"is a Factor")
        l.append(i)
    i+=1
print(l)
'''




#Prgm to read a number and reverse it


'''
a=int(input("Enter a number : "))
r=0
while a:
    d=a%10
    a//=10
    r=r*10+d

print (r)

'''



#Prgm for Palindrome

'''
a=int(input("Enter a number : "))
r=0
c=a
while a:
    d=a%10
    a//=10
    r=r*10+d
if r==c :
    print("Palindrome")
else:
    print("Not palindrome")
'''




#Prgm to print multiplication table of nos upto 10

'''
a=int(input("Enter a number : "))
for i in range(1,11):
    print(i,'*',a,'=',i*a)
        


'''


#Sum of n numbers (+ve and -ve separately)


'''
n=int(input("Limit : "))
s1=s2=0
for i in range(n):
    a=int(input("Number :"))
    if a%2==0 :
        s1+=a
    else :
        s2+=a
print("Sum of odd",s2,"Sum of even",s1)
'''



#Prime or not


'''
a=int(input())
if a<2:
    print("Not")
elif a==2:
    print("Prime")
elif a>2:
    for i in range(2,a):
        
        if a%i==0:
            print("Not")
            break
    else:
        print("Prime")
'''



'''
for i in range (6):
    for j in range (i):
        print(i,end='')
    print()



for i in range (6):
    for j in range (i,0,-1):
        print(j,end='')
    print()
print()

for i in range (6,0,-1):
    for j in range (1,i):
        print(j,end='')
    print()


for i in range (6,0,-1):
    for j in range (i,0,-1):
        print(j,end='')
    print()
'''




##Perfect number


'''
s=0
n=int(input("Enter a number : "))
for i in range(1,n):
    if n%i ==0:
        s+=i
if s==n :
    print("Perfect")

'''


##Factorial
'''
s=1
n=int(input("Enter a number : "))
for i in range(1,n+1):
    s*=i
print(s)


for i in range(1,4):
    for j in range(i+1):
        print(i,end=' ')
    print()
l=[1,2,3]
print( in )
'''


##Prgm to count the no of occurence of each letter in a sentence


'''
d={}
s='mekarakkattu gangadanpanikkar makal pooja'
for i in s:
    if i in d:
        d[i]+=1
    else :
        d[i]=1
print(d)
'''

##Prgm with slicing

'''
s='ComputerScience'
print(s[::2][::-1],s[::-1])
'''



##Prgm to count the frequency of occurence of 10 different random numbers
'''
l=[];d={} 
from random import *
for i in range(25):
    l.append(randrange(0,11))

for i in l:
    if i in d:
        
        d[i]+=1
    else :
        d[i]=1
print(d)
'''
'''
s=0
n=[1,2,3,4,5,6,7,8]
for k in n:
    for i in range(1,k):
        if k%i==0:
            s+=i
    if s==k:
        print(k)
'''

'''
l=[]
a=int(input("Enter a number : "))
while True :
    l.append(a)
    a=int(input("Enter a number : "))
print(l)
for i in range(len(l)):
    if l[i]%2!=0:
        c+=1
print("Number of odd elements :",c)
'''
'''
l=[]
lo=[]
le=[]
n=int(input("Limit : "))
for i in range(n):
    l.append(int(input("Enter a number : ")))
print(l)
for i in l:
    #n=l[i]
    if i%2==0:
        le.append(i)
    else:
        lo.append(i)

print(lo)
'''
'''
l=[]
lp=[]
n=int(input("Limit : "))
for i in range(n):
    l.append(int(input("Enter a number : ")))
print(l)
for i in l:
    for j in range(2,i):
        if i%j==0:
            break
    else:
        lp.append(i)

print(lp)
'''
'''
l=[]

n=int(input("Limit : "))
for i in range(n):
    l.append(int(input("Enter a number : ")))
print(l)
from math import *
for i in l:
    print(factorial(i))
'''

'''
l=[]
n=int(input("Limit : "))
for i in range(n):
    l.append(input("Enter a string: "))
print(l)
a=input("CH to be scearched : ")
for i in range(len(l)):
    if l[i]==a:
        l[i]=0
    else:
        l[i]=1
print(l)
'''            
'''   
l=[]
n=int(input("Limit : "))
for i in range(n):
    l.append(input("Enter a string: "))
print(l)
for i in range(0,len(l)-1,2):
    l[i],l[i+1]=l[i+1],l[i]
print(l)

'''
'''
t=()
for i in range(5):
    a=int(input("Enter a number : "))
    t+=(a,)
a=int(input("Enter a number : "))

for i in range(len(t)):
    if t[a]%2==0:
        print("Even")
        print(3*a+1)
        break
    else:
        print("Odd")
        print(a/2)
        break
'''        
    
#Prgm to find 1/1! + 1/2! + 1/3! + 1/! + 1/n! 
'''
s=1
from math import *
n=int(input("Number : "))
for i in range(1,n+1):
    s+=(1/factorial(n))
print(s)
'''














