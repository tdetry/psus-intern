"""

Find the Symmetric Difference
The mathematical term symmetric difference (△ or ⊕) of two sets is the set of elements which are in either of the two sets but not in both. 
For example, for sets A = {1, 2, 3} and B = {2, 3, 4}, A △ B = {1, 4}.

Symmetric difference is a binary operation, which means it operates on only two elements. 
So to evaluate an expression involving symmetric differences among three elements (A △ B △ C), you must complete one operation at a time. 
Thus, for sets A and B above, and C = {2, 3}, A △ B △ C = (A △ B) △ C = {1, 4} △ {2, 3} = {1, 2, 3, 4}.

"""

def symmetricDifference(list1, list2):
    """
    Returns the symmetric difference of two lists.
    """
    return list(set(list1) ^ set(list2))


def symmetricDifference_two(list):
    aux = []
    for element in list:
        aux = symmetricDifference(aux, element)
    return aux
        

if __name__ == "__main__":
    #lets create some lists 
    list1 = [1, 2, 3]
    list2 = [2, 3, 4]
    list3 = [2, 3, 4, 5]
    mayor_list = [list1, list2, list3]
    print(symmetricDifference([1, 2, 3], [2, 3, 4]))
    print(symmetricDifference_two(mayor_list))
