import os,sys

n=raw_input()
n=n.split()
n=int(n[0])
l=[0,1,2,6,24,120,720,4320] 
p=[]
def permute(a, i, n):
    if i==n:
        for i in a:
            print i,
        print
    else:
        for j in range(i,n+1):
            a[i],a[j]=a[j],a[i]
            permute(a, i+1, n)
            a[i],a[j]=a[j],a[i]


print l[n]
for i in range(1,n+1):
    p.append(i)

permute(p,0,n-1)

   
