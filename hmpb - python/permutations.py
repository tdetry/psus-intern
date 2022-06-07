'''
No Repeats Please

Return the number of total permutations of the provided string that don't have repeated consecutive letters. 
Assume that all characters in the provided string are each unique.

For example, aab should return 2 because it has 6 total permutations (aab, aab, aba, aba, baa, baa), but only 2 of them (aba and aba) 
don't have the same letter (in this case a) repeating.
'''

from itertools import permutations, pairwise
def getNumPermutation(string):
    per = (list(permutations(string)))
    result = len(per)
    for p in per:
        pairs = list(pairwise(p))
        for pair in pairs:
            pair = set(pair)
            if(len(pair) == 1):
                result -= 1
                break
    return result

print(getNumPermutation('aacb'))
        
