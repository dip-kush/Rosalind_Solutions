from string import translate, maketrans

f = open('rosalind_revp.txt', 'r')
raw_samples = f.readlines()
f.close()

dna = ''
for elem in raw_samples:
    if elem[0] == '>':
        pass
    else:
        dna+= elem.rstrip()



def revc(dnastring):
    translation = maketrans("ATCG", "TAGC")
    return translate(dnastring, translation)[::-1]


def revp(dna):
    for i in xrange(4, 12+1):
        for j in xrange(len(dna)-i+1):
            if dna[j:j+i] == revc(dna[j:j+i]):
                yield j+1, i


results=revp(dna)
for r in sorted(list(results)):
    print r[0],r[1]
