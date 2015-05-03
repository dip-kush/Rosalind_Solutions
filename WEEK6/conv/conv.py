f=open('rosalind_conv.txt')
a,b=f.readlines()
a,b=a.strip().split(),b.split()
a=map(float,a)
b=map(float,b)
c=[]
dic={}
for item in a:
    for item1 in b:
        c.append(round((item-item1),5))

for item in c:
    if item in dic.keys():
        dic[item]+=1
    else:
        dic[item]=1

max_val=max(dic.values())
keys = [x for x,y in dic.items() if y ==max_val]
print max_val
print  keys[0]

