from itertools import product
import os,sys
f=open('rosalind_kmer.txt', 'r')
lines=f.readlines()

b=['A','T', 'G', 'C']
i=-1
d=[]
for l in lines:
    if l[0]=='>':
        d.append('')
        i+=1
        continue
    else:
        d[i]+=l.strip()
dna=d[0]

kmer_list =  [''.join(kmer) for kmer in list(product('ACGT', repeat = 4))]

# Initialize the count of each 4-mer at zero for each 4-mer.
kmer_count = [0]*(4**4)

# Count each 4-mer
for i in range(len(dna)-3):
	kmer_count[kmer_list.index(dna[i:i+4])] += 1
for kmer_c in kmer_count:
	print kmer_c,



	
