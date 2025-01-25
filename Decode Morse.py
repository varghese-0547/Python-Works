



##For capitalizing and reverse operation
'''
D={}
for i in d:
    a=i.capitalize()
    b=d[i]
    D[b]=a
print(D)
'''





d={'.-':'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g',
   '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm',
   '-.': 'n', '---': 'o', '.--.':'p', '--.-': 'q', '.-.': 'r', '...': 's',
   '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y', '--..':'z'}


n=input("Str : ")
s=n.split(" ")
t=tuple(s)



A=''
for i in t:
    if i=='$':
        A+=' '
        continue

    
    if i in d:
        A+=d[i]
    else:
        A+=i
    
print(A)

