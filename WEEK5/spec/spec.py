import os,sys

f=open('monoiso_table.txt')
l=f.readlines()
dic={}
rev_dic={}
for item in l:
    i=item.strip().split()
    dic[i[0]]=round(float(i[1]),4)

for a,b in dic.iteritems():
    rev_dic[b]=a

#print dic
f=open('rosalind_spec.txt','r')
l=f.readlines()
for i in range(len(l)):
    l[i]=float(l[i].strip())

m=''
#print rev_dic
for i in range(1, len(l)):
    m+=rev_dic[round(l[i]-l[i-1],4)]
print m


