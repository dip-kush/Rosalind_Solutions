from numpy import zeros
f=open('rosalind_scsp.txt','r')
a,b=f.readlines()
a,b=a.strip(),b.strip()
m=len(a)
n=len(b)

def common_sub(x,y):
    m=[[(0,0) for i in range(len(y)+1)] for i in range(len(x)+1)]
    m[0][0]=0,0
    
def longest_common_subsequence(dna1, dna2):
    M = zeros((len(dna1)+1,len(dna2)+1))
    for i in xrange(len(dna1)):
        for j in xrange(len(dna2)):
            if dna1[i] == dna2[j]:
                M[i+1][j+1] = M[i][j]+1
            else:
                M[i+1][j+1] = max(M[i+1][j],M[i][j+1])

    longest_sseq = ''
    i,j = len(dna1), len(dna2)
    while i*j != 0:
        if M[i][j] == M[i-1][j]:
            i -= 1
        elif M[i][j] == M[i][j-1]:
            j -= 1
        else:
            longest_sseq = dna1[i-1] + longest_sseq
            i -= 1
            j -= 1

    return longest_sseq


i=0
j=0
final_str=''
while i < m and j < n:
    dna1,dna2=a[i:],b[j:]
    seq=longest_common_subsequence(dna1,dna2)
    if seq is not None:
        if seq[0]!=dna1[0]:
            final_str+=dna1[0]
            i+=1
        if seq[0]!=dna2[0]:
            final_str+=dna2[0]
            j+=1
        elif seq[0]==dna1[0] and seq[0]==dna2[0]:
            final_str+=dna1[0]
            i+=1
            j+=1
    else:
        final_str+=dna1[0]
        final_str+=dna2[0]
        i+=1
        j+=1
         
if i<m:
    final_str+=a[i:]
if j<n:
    final_str+=dna2[j:]

print final_str


