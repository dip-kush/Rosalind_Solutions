import re
import sys
from StringIO import StringIO
from Bio import SeqIO
import requests


if __name__ == '__main__':
    f = open("rosalind_mprt.txt","r")
    accs = f.readlines()
    
    for acc in accs:
        acc = acc.strip()
        r = requests.get('http://www.uniprot.org/uniprot/%s.fasta' % acc)
        s = SeqIO.read(StringIO(r.text), 'fasta')
        mos = [x for x in re.finditer(r'(?=(N[^P][ST][^P]))',  str(s.seq))]
        if not len(mos):
            continue
        print(acc)
        print(' '.join([str(mo.start(0) + 1) for mo in mos]))
