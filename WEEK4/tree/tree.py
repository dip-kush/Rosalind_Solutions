import os,sys
f=open('rosalind_tree.txt','r')
l=f.readlines()
print int(l[0].strip())-len(l)
