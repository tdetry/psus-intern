#Find the Symmetric Difference
'''
The mathematical term symmetric difference (△ or ⊕) of two sets is the set of elements which are in either of the two sets but not in both. 
For example, for sets A = {1, 2, 3} and B = {2, 3, 4}, A △ B = {1, 4}.

Symmetric difference is a binary operation, which means it operates on only two elements. 
So to evaluate an expression involving symmetric differences among three elements (A △ B △ C), you must complete one operation at a time. T
hus, for sets A and B above, and C = {2, 3}, A △ B △ C = (A △ B) △ C = {1, 4} △ {2, 3} = {1, 2, 3, 4}.

Create a function that takes two or more list and returns an list of their symmetric difference. 
The returned list must contain only unique values (no duplicates).
'''

def SymetricDifference(list1): 
    A = set(list1[0])
    B = set(list1[1])
    result = A.symmetric_difference(B)
    if(len(list1)>2):
        for arr in list1[2:]:
            result = result.symmetric_difference(set(arr))
    return(list(result))

A = [1, 2, 3]
B = [5, 2, 1, 4]
C = [1]
D = [1,5,6]
E = [7,8] 
print(SymetricDifference([A,B,C,D,E]))
