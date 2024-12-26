





s=input('String : ')
v=''
for i in s:
    v+=chr(ord(i)-1)
print(v)







##Trial
'''
d={'a':'z','z':'y','y':'x','x':'w','w':'v','v':'u','u':'t','t':'s','s':'r','r':'q','q':'p','p':'o','o':'n','n':'m','m':'l','l':'k','k':'j','j':'i','i':'h','h':'g','g':'f','f':'e','e':'d','d':'c','c':'b','b':'a'}
D={'A': 'Z', 'Z': 'Y', 'Y': 'X', 'X': 'W', 'W': 'V', 'V': 'U', 'U': 'T', 'T': 'S', 'S': 'R', 'R': 'Q', 'Q': 'P', 'P': 'O', 'O': 'N', 'N': 'M', 'M': 'L', 'L': 'K', 'K': 'J', 'J': 'I', 'I': 'H', 'H': 'G', 'G': 'F', 'F': 'E', 'E': 'D', 'D': 'C', 'C': 'B', 'B': 'A'} 
S=input('String : ')
A=''
for i in range(len(S)):
    if S[i] in D:
        A+=D[S[i]]
    else:
        A+=d[S[i]]
print(A)
'''



