sr = input("enter a sring: ")
def split(sr): 
    return list(sr)
A = split(sr)
S = sorted(A,reverse=True)
#print(S)
c = ''.join(S)
print(c)



