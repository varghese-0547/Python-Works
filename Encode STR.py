
##Simple code
'''
s=input('String : ')
v=''
for i in s:
    v+=chr(ord(i)+1)
print(v)

'''


##Prgm to get the dictionary in capital letters
'''
##d={'a':'z','z':'y','y':'x','x':'w','w':'v','v':'u','u':'t','t':'s','s':'r','r':'q','q':'p','p':'o','o':'n','n':'m','m':'l','l':'k','k':'j','j':'i','i':'h','h':'g','g':'f','f':'e','e':'d','d':'c','c':'b','b':'a'}
##D={}
##for i in d:
##    a=i.capitalize()
##    b=d[i].capitalize()
##    D[a]=b
##print(D)



##s="'a':'b','b':'c','c':'d','d':'e','e':'f','f':'g','g':'h','h':'i','i':'j','j':'k','k':'l','l':'m','m':'n','n':'o','o':'p','p':'q','q':'r','r':'s','s':'t','t':'u','u':'v','v':'w','w':'x','x':'y','y':'z','z':'a'"
##print(s[::-1])


'''

d={'a':'b','b':'c','c':'d','d':'e','e':'f','f':'g','g':'h','h':'i','i':'j',
   'j':'k','k':'l','l':'m','m':'n','n':'o','o':'p','p':'q','q':'r','r':'s',
   's':'t','t':'u','u':'v','v':'w','w':'x','x':'y','y':'z','z':'a'}


D={'A': 'B', 'B': 'C', 'C': 'D', 'D': 'E', 'E': 'F', 'F': 'G', 'G': 'H',
   'H': 'I', 'I': 'J', 'J': 'K', 'K': 'L', 'L': 'M', 'M': 'N', 'N': 'O',
   'O': 'P', 'P': 'Q', 'Q': 'R', 'R': 'S', 'S': 'T', 'T': 'U', 'U': 'V',
   'V': 'W', 'W': 'X', 'X': 'Y', 'Y': 'Z', 'Z': 'A'}


S=input('String : ')
A=''
for i in range(len(S)):
    if S[i] in D:
        A+=D[S[i]]
    else:
        A+=d[S[i]]
print(A)

