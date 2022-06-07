#Exercise 1
print("#### Exercise 1 ####")
#Count the occurrence of each element from a list

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89, 100, 100, 101]

def exercise1(sample_list):
    result = {}
    for element in sample_list:
        if element in result:
            result[element] += 1
        else:
            result[element] = 1
    return result

print(exercise1(sample_list))


#Exercise 2
print("\n#### Exercise 2 ####\n")
#Create a python set such that it shows the element from both lists in a pair

list1 = [2, 3, 4, 5, 6, 7, 8]
list2 = [4,9,16,25,36,49,64]

result = set(zip(list1, list2))
print(result)

#Exercise 3
print("\n#### Exercise 3 ####\n")
#Find the intersection of two sets and remove those elements from the first set

set1 = {23, 42, 65, 57, 78, 83, 29}
set2 = {57, 83, 29, 67, 73, 43, 48}

def exercise3(set1, set2):
    intersection = set1.intersection(set2)
    for element in intersection:
        set1.remove(element)
    print(f"The intersection set is: {intersection} and the first set without intersection is: {set1}")

exercise3(set1, set2)

#Exercise 4
print("\n#### Exercise 4 ####\n")
#Iterate a given list and check if a given element exists as a key's value in a dictionary. If not, delete it from the list

list1 = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma': 69, 'Kelly':76, 'Jason':97}

def exercise4(list, sample_dict):
    to_delete = []
    for element in list:
        if element not in sample_dict.values():
            to_delete.append(element)
    for element in to_delete:
        list.remove(element)
    print(f"Values in dict are: {list}")

exercise4(list1, sample_dict)

#Exercise 5
print("\n#### Exercise 5 ####\n")
#Get all values from the dictionary and add them to a list but don't add duplicates

speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

def exercise5(speed):
    return list(set(speed.values()))

print(f"Values with no duplicates: {exercise5(speed)}")

#Exercise 6
print("\n#### Exercise 6 ####\n")
#Remove items greater than X from a list while iterating without creating a different copy of a list

list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
x = 50

def exercise6(list, x):
    i = 0
    n = len(list)
    while i<n:
        if list[i] > x:
            del list[i]
            n -= 1
        else:
            i += 1
    return list

print(f"List without numbers greater than {x}: {exercise6(list1, x)}")

#Exercise 7
print("\n#### Exercise 7 ####\n")
#Reverse Dictionary mapping

ascii_dict = {'A': 65, 'B': 66, 'C':67}

def exercise7(dict):
    return {value: key for key, value in dict.items()}

print(f"Reversed Dictionary: {exercise7(ascii_dict)}")

#Exercise 8
print("\n#### Exercise 8 ####\n")
#Display all duplicate items from a list

import collections

sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]

def exercise8(list):
    result = []
    for element, count in collections.Counter(list).items():
        if count > 1:
            result.append(element)
    return result

print(f"The duplicated elements in the list are: {exercise8(sample_list)}")





