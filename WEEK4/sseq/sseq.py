import os,sys
f=open('rosalind_sseq.txt', 'r')
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

l=[]
j=0


def get_indices(s,t):
    indices = []


    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            indices.append(i + 1)
            j += 1
        i += 1

    return indices

ind=get_indices(d[0],d[1])

for i in ind:
	print i,

		
