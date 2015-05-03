import os,sys
data=raw_input()
data = data.split()
n=int(data[0])
k=int(data[1])
a=0
b=1
for i in range(n-1):
    c=b+k*a
    a=b
    b=c
if n==1:
    c=1
print c
