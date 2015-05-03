import os,sys
from math import factorial
f=open('rosalind_mmch.txt', 'r')
lines=f.readlines()

dna=''
for l in lines:
    if l[0]=='>':
        continue
    else:
        dna+=l.strip()



def get_basepair_edges(rna):
    a, u, g, c = map(rna.count, ["A", "U", "G", "C"])
    
    a = factorial(max(a, u)) / factorial(max(a, u) - min(a, u))
    b = factorial(max(g, c)) / factorial(max(g, c) - min(g, c))
    
    return a * b

	
print get_basepair_edges(dna)
