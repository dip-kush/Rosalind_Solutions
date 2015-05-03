import os,sys
f=open('rosalind_seto.txt', 'r')
lines=f.readlines()

i=-1
d=[]
for l in lines:
    d.append(l.strip())
n=int(d[0])
a=d[1].split(', ')
b=d[2].split(', ')
a[0]=a[0][1:]
b[0]=b[0][1:]
#a[-1]=a[-1][0:-2]
b[-1]=b[-1][0:-1]
a[-1]=a[-1][0:-1]
c=set()
d=set()
a=map(int, a)
b=map(int, b)

u=set()
for item in a:
    c.add(item)
for item in b:
    d.add(item)
for i in range(1,n+1):
    u.add(i)

def print_curly(s):
    print "{"+', '.join(map(str,s))+'}'



print_curly(c.union(d))
print_curly(c.intersection(d))
print_curly(c.difference(d))
print_curly(d.difference(c))
print_curly(u.difference(a))
print_curly(u.difference(b))
