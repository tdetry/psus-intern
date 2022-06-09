Enter Python code here and hit the Run button.

for i in range(1,6):
    for j in range(6-i,0,-1):
        print(i, end=' ')
    print()
   
def outer(x,y):
    def inner():
        return x + y
    return inner() + 'Developer'
   
result = outer('Emma', 'Kelly')
print(result)

str = 'My Name is Jessa'
rev_list = [x[::-1] for x in str.split()]
print(" ".join(rev_list))

sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
s = set()
dups = set()
for e in sample_list:
    if (e in s):
        dups.add(e)
    else:
        s.add(e)
print(dups)

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
dict = {}
for e in sample_list:
    if e not in dict:
        dict[e] = 1
    else:
        dict[e] += 1
print(dict)

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
list = [x for x in roll_number if x in sample_dict.values()]
print(list)

str1 = "Apple"
dict = {}
for ch in str1:
    dict[ch] = str1.count(ch)
print(dict)

def twoNumberSum(array, targetSum):
    ret = []
    s = set(array)
    for e in array:
        s.remove(e)
        if targetSum - e in s:
            return [e, targetSum - e]
    return []

def threeNumberSum(array, targetSum):
    ret = []
    array.sort()
    s = set(array)
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            s = set(array[j+1:])
            if targetSum - array[i] - array[j] in s:
                l = [array[i], array[j], targetSum - array[i] - array[j]]
                ret.append(l)
    return ret

def isValidSubsequence(array, sequence):
    index_arr = 0
    index_sub = 0
    while (index_arr < len(array) and index_sub < len(sequence)):
        if (array[index_arr] == sequence[index_sub]):
            index_sub += 1
        index_arr += 1
    if (index_sub == len(sequence)):
        return True
    return False

def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    index1 = 0
    index2 = 0
    min = 999999
    ret = []
    while (index1 < len(arrayOne) and index2 < len(arrayTwo)):
        elem1 = arrayOne[index1]
        elem2 = arrayTwo[index2]
        if (elem1 < elem2):
            if (elem2 - elem1 < min):
                min = elem2 - elem1
                ret = [elem1, elem2]
            index1 += 1
        elif (elem1 > elem2):
            if (elem1 - elem2 < min):
                min = elem1 - elem2
                ret = [elem1, elem2]
            index2 += 1
        else:
            return [elem1, elem2]
        
    return ret

def moveElementToEnd(array, toMove):
    idx = 0
    to_add = 0
    length = len(array)
    while (idx < length - to_add):
        if (array[idx] == toMove):
            array.pop(idx)
            to_add += 1
            continue
        idx += 1
    for i in range(to_add):
        array.append(toMove)
    return array
    
def isMonotonic(array):
    if (len(array) == 0 or len(array) == 1 or len(array) == 2):
        return True
    for i in range(len(array) - 1):
        array[i] = array[i + 1] - array[i]
    array[len(array) - 1] = 0
    print(array)
    prod = 1
    sign = 999
    for e in array:
        if e != 0:
            if (sign == 999):
                sign = e/abs(e)
            else:
                if (sign != e/abs(e)):
                    return False
    return True
            
