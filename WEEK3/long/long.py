def find_overlaps(arr, acc=''):
    if len(arr) == 0:
        return acc

    elif len(acc) == 0:
        acc = arr.pop(0)
        return find_overlaps(arr, acc)

    else:

        for i in range(len(arr)):
            a = arr[i]
            l = len(a)

            for p in range(l / 2):
                q = l - p
                
                if acc.startswith(a[p:]):
                    arr.pop(i)
                    return find_overlaps(arr, a[:p] + acc)

                if acc.endswith(a[:q]):
                    arr.pop(i)
                    return find_overlaps(arr, acc + a[q:])


if __name__ == "__main__":
    large_dataset = open('rosalind_long.txt')
    raw_samples=large_dataset.readlines()
    dna=[]
    i=-1
    for elem in raw_samples:
        if elem[0] == '>':
            dna.append('')
            i+=1
        else:
            dna[i]+=elem.rstrip()

    print find_overlaps(dna)


