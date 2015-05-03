f=open('rosalind_rstr.txt','r')
l=f.readlines()
val=l[0].strip().split()
dna=l[1].strip()
N=int(val[0])
gc_content=float(val[1])

codon_count = [0, 0]
for codon in dna:
	if codon in ['C', 'G']:
		codon_count[0] += 1
	elif codon in ['A', 'T']:
		codon_count[1] += 1


dna_prob = ((0.5*gc_content)**codon_count[0])*((0.5*(1-gc_content))**codon_count[1])

prob = 1 - (1-dna_prob)**N

print prob
