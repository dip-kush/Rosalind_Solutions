import os,sys
f=open('rosalind_kmp.txt', 'r')
lines=f.readlines()

i=-1
dna=''
for l in lines:
    if l[0]=='>':
        continue
    else:
        dna+=l.strip()

P = [0]*len(dna)
k = 0
for q in range(2, len(dna)):
    while k > 0 and dna[k] != dna[q-1]:
        k = P[k-1]
    if dna[k] == dna[q-1]:
        k += 1
    P[q-1] = k

for i in P:
	print i,
