import math
f=open('rosalind_aspc.txt')
a,b=map(int,f.read().strip().split())



def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)
s=0
for i in range(b,a+1):
    s+=nCr(a,i)
print s%1000000
