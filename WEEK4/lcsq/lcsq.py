from numpy import zeros
import os,sys
f=open('rosalind_lcsq.txt', 'r')
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


def longest_common_subsequence(dna1, dna2):
	M = zeros((len(dna1)+1,len(dna2)+1))
	for i in xrange(len(dna1)):
		for j in xrange(len(dna2)):
			if dna1[i] == dna2[j]:
				M[i+1][j+1] = M[i][j]+1
			else:
				M[i+1][j+1] = max(M[i+1][j],M[i][j+1])

	longest_sseq = ''
	i,j = len(dna1), len(dna2)
	while i*j != 0:
		if M[i][j] == M[i-1][j]:
			i -= 1
		elif M[i][j] == M[i][j-1]:
			j -= 1
		else:
			longest_sseq = dna1[i-1] + longest_sseq
			i -= 1
			j -= 1

	return longest_sseq

	
	
lcsq = longest_common_subsequence(d[0],d[1])
print lcsq
