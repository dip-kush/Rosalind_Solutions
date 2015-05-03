import os,sys

dna1 = raw_input()
dna2 = raw_input()

l = len(dna1)

count=0
for i in range(l):
    if dna1[i] != dna2[i]:
        count+=1
print count
