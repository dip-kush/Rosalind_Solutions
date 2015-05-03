import os,sys
f=open('rosalind_tran.txt', 'r')
lines=f.readlines()
i=-1
dna=[]
for l in lines:
    if l[0]=='>':
		i+=1;
		dna.append('')
    else:
        dna[i]+=l.strip()

first=dna[0]
second=dna[1]

dic={'A':'G','C':'T','G':'A','T':'C'}
trans=0.0
travs=0.0

for i in range(len(first)):
	if first[i]==second[i]:
		pass
	elif dic[first[i]]==second[i]:
		trans+=1
	else:
		travs+=1
print trans/travs
