i=raw_input()
i=i.split()




def binomial(n, k):
    if k > n - k:
        k = n - k  # Use symmetry of Pascal's triangle
    accum = 1
    for i in range(1, k + 1):
        accum *= (n - (k - i))
        accum /= i
    return accum


def P(n, k):
    return binomial(2**k, n) * 0.25**n * 0.75**(2**k - n)


def problem(k, N):
    return 1 - sum([P(n, k) for n in range(N)])

print problem(int(i[0]), int(i[1]))
