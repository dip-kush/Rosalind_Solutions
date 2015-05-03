import sys,os
f = open('rosalind_grph.txt', 'r')
raw_samples = f.readlines()
f.close()

samples = {}
cur_key = ''
i=-1
k=[]
v=[]
for elem in raw_samples:
    if elem[0] == '>':
        cur_key = elem[1:].rstrip()
        k.append(cur_key)
        v.append('')
        i+=1
    else:
        v[i]+= elem.rstrip()





for i in range(len(k)):
    for j in range(i+1,len(k)):
        if v[i][-3:]==v[j][0:3] or v[i][0:3]==v[j][-3]:      
            print k[i],k[j]

            
            

