'''
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).

'''

def find_it(seq):
    if len(seq) == 1:
        return seq[0]
    
    result = 0
    my_dict = {}
    for i in range(len(seq)):
        current = seq[i]
        if str(current) in my_dict:
            my_dict[str(current)] = my_dict[str(current)] + 1
        else:
            my_dict[str(current)] = 1

    for i in my_dict:
        if my_dict[i] % 2 == 1:
            result = i

    return int(result)


print(find_it([7])) # Expected: 7
print(find_it([0])) # Expected: 0
print(find_it([1,1,2])) # Expected: 2
print(find_it([0,1,0,1,0])) # Expected: 0
print(find_it([1,2,2,3,3,3,4,3,3,3,2,2,1])) # Expected: 0
print(find_it([5,4,3,2,1,5,4,3,2,10,10]))