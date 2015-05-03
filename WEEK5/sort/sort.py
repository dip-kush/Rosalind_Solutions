def breakpoint_count(permutation):
    '''Returns the number of breakpoints in a given permutation.'''

    
    permutation = [0] + list(permutation) + [len(permutation)+1]

    return sum(map(lambda x,y: abs(x-y) != 1, permutation[1:], permutation[:-1]))


def breakpoint_indices(permutation):
    '''Returns the indices of all breakpoints in a given permutation.'''
    from itertools import compress
    
    permutation = [0] + list(permutation) + [len(permutation)+1]

    return compress(xrange(len(permutation)-1), map(lambda x,y: abs(x-y) != 1, permutation[1:], permutation[:-1]))


def greedy_breakpoint_bfs_sort(permutation):
    '''Performs a greedy breakpoint reduction based BFS sorting of a given permutation.'''
    from itertools import product

    
    rev_perm = lambda perm, i, j: perm[:i] + perm[i:j+1][::-1] + perm[j+1:]

    
    permutation = tuple(permutation)
    current_perms = {permutation:[]}
    min_breaks = breakpoint_count(permutation)

    
    while True:
        new_perms = {}
    
        for perm in current_perms.keys():
            for rev_ind in product(breakpoint_indices(perm), repeat=2):
    
                temp_perm = tuple(rev_perm(perm, rev_ind[0], rev_ind[1]-1))
                temp_breaks = breakpoint_count(temp_perm)
                temp_transformation = current_perms[perm] + [str(rev_ind[0]+1) + ' ' + str(rev_ind[1])]

    
                if temp_breaks == 0:
                    return temp_transformation

    
                elif temp_breaks < min_breaks:
                    min_breaks = temp_breaks
                    new_perms = {temp_perm:temp_transformation}

    
                elif temp_breaks == min_breaks:
                    new_perms[temp_perm] = temp_transformation

        current_perms = new_perms



    
with open('rosalind_sort.txt') as input_data:
    perms = [map(int, line.strip().split()) for line in input_data.readlines()]


to_identity = {value:i+1 for i, value in enumerate(perms[1])}
normalized_perm = [to_identity[value] for value in perms[0]]


min_reversal = greedy_breakpoint_bfs_sort(normalized_perm)


min_reversal = [str(len(min_reversal))] + min_reversal


print '\n'.join(min_reversal)
