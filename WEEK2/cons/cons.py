import os,sys

f=open('rosalind_cons.txt','r')
l=f.readlines()
g=[]
i=-1;
for elem in l:
    if elem[0]=='>':
        i+=1
        g.append('')
        continue
    else:
        g[i]+=elem.strip()

str_len=len(g[0])
m=[]
for i in range(str_len):
    m.append(' ')

for elem in g:
    for i in range(str_len):
        m[i]+=elem[i]
n=[]
for elem in m:
    count_a=elem.count('A')
    count_g=elem.count('G')
    count_c=elem.count('C')
    count_t=elem.count('T')
    tup = {'A':count_a,'G':count_g,'C':count_c,'T':count_t}
    n.append(tup)

final_str=''
for d in n:
    val=max(d, key=d.get)
    final_str+=val
print final_str

A=['A:']
G=['G:']
C=['C:']
T=['T:']
for elem in n:
    A.append(elem['A'])
    G.append(elem['G'])
    C.append(elem['C'])
    T.append(elem['T'])
for elem in A:
    print elem,
print 

for elem in C:
    print elem,
print 
for elem in G:
    print elem,
print
for elem in T:
    print elem,
print
       
    

            
    

