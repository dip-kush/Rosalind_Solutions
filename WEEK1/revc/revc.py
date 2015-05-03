import os,sys

dna=raw_input()
dna=dna[::-1]
l=list(dna)
for i in range(len(l)):
    if l[i]=='A':
        l[i]='T' 
    elif l[i]=='T':
        l[i]='A'
    elif l[i]=='G':
        l[i]='C'
    elif l[i]=='C':
        l[i]='G'

dna=''.join(l)
        
        

print dna
        
