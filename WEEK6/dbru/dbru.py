f=open('rosalind_dbru.txt')
l=f.read().strip()
l=l.split()
m=set()

lookup={'A':'T','T':'A','G':'C','C':'G'}
for item in l:
    m.add(item)
    m.add(''.join([lookup[c] for c in reversed(item)]))
m=sorted(m)
s=len(l[0])
for item in m:
    print '('+item[0:s-1]+", "+item[1:]+")"
