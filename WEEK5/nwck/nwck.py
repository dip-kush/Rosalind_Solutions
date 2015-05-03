f=open('rosalind_nwck.txt')

l=f.read().strip()

l=l.split('\n\n')

m=[]
def maintain_index(s):
    dic={}
    i=0
    for item in s:
        if item=='(':
            m.append(i)
        elif item==')':
            dic[i]=m.pop()
        i+=1
    return dic

def maintain_index1(s):
    dic={}
    i=len(s)-1
    ''.join([c for c in reversed(item)])
    for item in s:
        if item==')':
            m.append(i)
        elif item=='(':
            dic[i]=m.pop()
        i-=1
    return dic



def calculate(s):
    a,b=s.split('\n')    
    b,c=b.split()  
    st_index=0
    end_index=len(a)
    b_index,c_index=a.find(b),a.find(c) 
    #print b_index, c_index 
    tempb,tempc=b_index,c_index
    dic=maintain_index(a)
    c1,c2=0,0
    #print dic
    while True:
        q=a.find(')',b_index+1)
        if q!=-1:
            r=dic[q]
            if (a[r:q].find(c))!=-1:
                c1+=1
                break
            b_index=q
            if r < tempb:
                c1+=1
                continue
        else:
            break
    while True:
        q=a.find(')',c_index+1)
        if q!=-1:
            r=dic[q]
            c_index=q
            if a[r:q].find(b)!=-1:
                c2+=1
                break
            if r < tempc:
                c2+=1
                continue
        else:
            break
    return c1+c2        
     
for item in l:
    print calculate(item),
  

