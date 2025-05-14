
'''
l=[1,2,3]
n=[4,5,6]
a=[8,9,0]
print(l,n,a)
'''



##n=[]
##while True:
##    a=int(input("Enter element : "))
##    if a==0:
##        break
##    n.append(a)
##
##for i in range(len(n)):
##    if n[i]%2==0:
##        n[i]=n[i]*2
##    else :
##        n[i]=n[i]*3
##    #print(n)
##print(n)
##print(len(n))



'''
for i in range(5):
    for j in range(1,i+1):
        print(i,end=' ')
    print()
'''

'''
for i in range(1,6):
    print(0,0,0,0,sep='0')
    


for i in range(5):
    print(0,0,0,0,end=' ')
'''


'''
a,b=0,1
print(a)
for i in range(10):
    print(b)
    a,b=b,a+b


s=" i love India. it is the best"
print(s)
##for i in range(len(s)):
##    print(i,s[i],sep='  ')

print(s.index(' ',1))
'''



'''
s=input("Serinjg : ")

for i in range(len(s)):
    a=s[i].lower()
    print(ord(a))
'''
'''
d={'MAT':'AGN',
   'CHEM':'LV',
   'PHY':'LKN',
   'CS':'ST'}
for i in d:
    print(i,' ',d[i])

'''
'''
l=[]
n=int(input("Limit : "))
for i in range(n):
    l.append(int(input("Number : ")))
d={}
for i in l:
    d[i]=l.count(i)
print(d)

'''


##'''
##t1=(1,2,3,4,5,6,7,8)
##print(t1[-2:-5:-1])
##for i in t1[-2:-5:1]:
##    print(i)
##
##'''
'''

t1=((45,67,98))
print(type(t1))
t2=(45,67,98)
print(t1[0] in t2)
print()
print(45 in t2)
print()
print(45 in t1)
print()
print(t2 in t1)
print()
print(t1 == t2)
'''


'''
t1=("happy",)
for i in t1:
    print(i+i)
'''
'''
##Prgm to count the no of each letter in a sentence
d={}
s='mekarakkattu gangadanpanikkar makal pooja'
for i in s:
    if i in d:
        d[i]+=1
    else :
        d[i]=1
print(d)
'''
'''
s='ComputerScience'
print(s[::2][::-1],s[::-1])
'''



'''
l=[];d={} 
from random import *
from statistics import *
for i in range(25):
    l.append(randrange(0,11))
print(mean(l))
for i in l:
    if i in d:
        
        d[i]+=1
    else :
        d[i]=1
print(d)
'''


'''d={1: ['VG', 45], 2: ['MG', 40], 3: ['DR', 35], 7:['gg',40]}
D={4: ['VG', 45], 5: ['MG', 40], 6: ['DR', 35]}
####for i in range(3): 
####    n=int(input("Roll No. : "))
####    na=input("Name : ")
####    n1=int(input("Mark : "))
####    d[n]=[na,n1]
#print(d)
d.update(D)
print(d.values())
print(d.get(2,'no'))'''
l=['apple','kiwi','banana']
##d={}
##for i in l:
##    d[len(i)]=i
##d1=dict(sorted(d.items()))
##print(list(d1.values()))
print(l)

print(sorted(l))
print(l)











