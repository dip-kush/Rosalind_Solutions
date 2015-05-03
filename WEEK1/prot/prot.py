def codon_table():
    f = open('codon_table.txt', 'r')
    codontable = f.readlines()
    f.close()
    c = dict()
    for k, v in [elem.split() for elem in codontable]:
        c[k] = v
    return c

f = open('rosalind_prot.txt', 'r')
rna = f.readline()
f.close()

rna = rna.rstrip()
protein = []
codon = codon_table()
for i in range(0, len(rna), 3):
    protein.append(codon[rna[i:i+3]])
print ''.join(protein[:-1])


