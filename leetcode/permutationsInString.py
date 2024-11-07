from itertools import permutations

def permutationsString(s1, s2):
    for perm in [''.join(p) for p in permutations(s1)]:
        if perm in s2:
            return True
    return False



print(permutationsString('ab', 'eidbaooo'))