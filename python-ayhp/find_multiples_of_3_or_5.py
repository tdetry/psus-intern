'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. Additionally, if the number is negative, return 0 (for languages that do have them).

Note: If the number is a multiple of both 3 and 5, only count it once.

Input: 200
Output: 9168
Input: -1
Output: 0
Input: 20
Output: 78
Input: 15
Output 45
'''

import functools

def solution(number):
    res = []
    if number < 0: 
        return 0

    for x in range(number):
        if x % 3 == 0 or x % 5 == 0:
            res.append(x)
    
    return functools.reduce(lambda a,b: a + b, res, 0)

print(solution(200)) # Expected: 9168
print(solution(-1)) # Expected: 20
print(solution(20)) # Expected: 78
print(solution(15)) # Expected: 45
