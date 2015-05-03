import os,sys
f=open('rosalind_edit.txt', 'r')
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

str1=d[0]
str2=d[1]

m=[[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]


m[0][0]=0

for i in range(len(str1)+1):
	m[i][0]=i;
for j in range(len(str2)+1):
	m[0][j]=j
x=len(str1)
y=len(str2)
for i in range(1, x+1):
	for j in range(1, y+1):
		m[i][j]=min(m[i-1][j-1]+(str1[i-1]!=str2[j-1])*1, m[i-1][j]+1, m[i][j-1]+1)

print m[x][y]

'''
m[i,j] = d(s1[1..i], s2[1..j])

m[0,0] = 0
m[i,0] = i,  i=1..|s1|
m[0,j] = j,  j=1..|s2|

m[i,j] = min(m[i-1,j-1]
             + if s1[i]=s2[j] then 0 else 1 fi,
             m[i-1, j] + 1,
             m[i, j-1] + 1 ),  i=1..|s1|, j=1..|s2|
'''
