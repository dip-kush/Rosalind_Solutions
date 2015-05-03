import os,sys

dna=raw_input()
t=raw_input()

dna_len=len(dna)
t_len=len(t)
i=0
l=[]
while i<dna_len:
    f=dna.find(t,i)
    if f==-1:
        break
    else:
        l.append(f+1)    
        i=f+1

for item in l:
    print item,
