def alpha_combs(alphabet, n, acc='', res=[]):
    if n > 0:
        for c in alphabet:
            res.append(acc + c)
            alpha_combs(alphabet, n - 1, acc + c, res)
    return res


f = open('rosalind_lexv.txt')
l=f.readlines()
alpha=l[0].strip().split()
n=int(l[1].strip())
g=alpha_combs(alpha,n)
for item in g:
	print item
