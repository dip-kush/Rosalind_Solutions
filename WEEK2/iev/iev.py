import os,sys


prob=raw_input()
l=prob.split()
p=[2, 2, 2, 1.5, 1, 0]

tot=0.0;
for i in range(6):
    item = float(l[i])
    tot+=(item*p[i])

print tot
    
    
