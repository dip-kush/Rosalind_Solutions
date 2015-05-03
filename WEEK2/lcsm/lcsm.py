import sys,os
f = open('rosalind_lcsm.txt', 'r')
raw_samples = f.readlines()
f.close()

samples = {}
cur_key = ''
i=-1
v=[]
for elem in raw_samples:
    if elem[0] == '>':
        v.append('')
        i+=1
    else:
        v[i]+= elem.rstrip()




def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and is_substr(data[0][i:i+j], data):
                    substr = data[0][i:i+j]
    return substr

def is_substr(find, data):
    if len(data) < 1 and len(find) < 1:
        return False
    for i in range(len(data)):
        if find not in data[i]:
            return False
    return True


print long_substr(v)
