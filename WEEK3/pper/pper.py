import math
f=open('rosalind_pper.txt')
l=f.readlines()

for i in l:
    g = i.strip().split()

n=int(g[0])

k=int(g[1])

numo=math.factorial(n)
mod=1000000
def fast_pow(base, n , M):
    if n==0:
        return 1
    if n==1:
        return base
    halfn=fast_pow(base, n/2, M)
    if n%2==0:
        return (halfn*halfn)%M
    else:
        return (((halfn*halfn)%M)*base)%M


deno=math.factorial(n-k)
print (numo/deno)%mod



