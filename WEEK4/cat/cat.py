def noncrossing_perfect_bondings(rna):
    bonding = {'A':'U', 'U':'A', 'C':'G', 'G':'C'}
    noncrossing_bondings = {}

    def count_noncrossing(rna):
        if len(rna) <= 2:  
            return 1
        elif rna in noncrossing_bondings:  
            return noncrossing_bondings[rna]

        splits = [i for i in xrange(1, len(rna), 2) if rna[0] == bonding[rna[i]] and check_subinterval(rna[1:i])]

        noncrossing_bondings[rna] = sum([count_noncrossing(rna[1:i])*count_noncrossing(rna[i+1:]) for i in splits]) % 1000000

        return noncrossing_bondings[rna]

    return count_noncrossing(rna)


def check_subinterval(subint):
    N = [subint.count(nucleotide) for nucleotide in 'AUCG']
    return N[0] == N[1] and N[2] == N[3] 



import os,sys
f=open('rosalind_cat.txt', 'r')
lines=f.readlines()

i=-1
d=[]
for l in lines:
    if l[0]=='>':
        d.append('')
        i+=1
        continue
    else:
        d[i]+=l.strip()
   
noncrossing = str(noncrossing_perfect_bondings(d[0]))

print noncrossing
