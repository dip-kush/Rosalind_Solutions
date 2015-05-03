import sys,os

f = open('mass_table.txt','r')
lines=f.readlines()
d={}
for i in lines:
    i=i.strip().split()
    d[i[0]]=i[1]
input_file=open('rosalind_prtm.txt','r')
l=input_file.readlines()
m=0.0
t=0.0
for i in l:
    i=i.strip()
    for j in i:
        m+=float(d[j])
print round(m,3)   
