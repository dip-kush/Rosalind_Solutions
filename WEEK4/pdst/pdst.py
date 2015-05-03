import os,sys

f=open('rosalind_pdst.txt', 'r')
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

def diff(a,b):
	count=0.00000
	count+=abs(len(a)-len(b))
	for i in range(len(a)):
		if a[i]!=b[i]:
			count+=1
	return count

ans=[]
for a in d:
	for b in d:
		ans.append("{:.5f}".format(diff(a,b)/min(len(a),len(b))))
i=0
while i<len(ans):
	for j in range(len(d)):
		print ans[i],
		i+=1
	print
	
