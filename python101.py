##### Lists #####
print("\n##### Lists #####\n")
list1 = list(range(10))
print(list1)
list1.reverse()
print(list1)



list1 = ["M", "na", "i", "Je"] 
list2 = ["y", "me", "s", "rry"]
list3 = [x + y for x, y in zip(list1, list2)]
print(*list3)


##### Tuples #####
print("\n##### Tuples #####\n")
a, b, c = (1, 2, 3)
print(b)
a, *b, c = tuple(range(10))
print(b)
print(a, c)
a, c = c, a
print(a, c)


##### Dictionaries #####
print("\n##### Dictionaries #####\n")
empty = {}
dict1 = {"one": 1, "two": 2}
print(dict1["one"])
print(dict1.items())
print(dict1.keys())

dict1.setdefault("three", 3)
print(dict1["three"])

dict2 = {'a': 1, **{'b': 2}}
print(dict2.items())

##### Sets #####
print("\n##### Sets #####\n")
set1 = {1,2,3,4,3,4,5}
print(len(set1))
set1.add(6)
set2 = {4,6,7}
print(set1 & set2)
print(set1 | set2)
print(set1 - set2)
print({1, 2} >= {1, 2, 3})
print({1, 2} <= {1, 2, 3})
print(3 in set1)

##### Others #####
print("\n##### Others #####\n")

x = [[0 for x in range(10) for x in range(5) if x==2]]
y = tuple(0 for y in range(10) for y in range(5) if y==2)
print(x, y)


def func(*args):
    print(*args)

x = (1,23,23423,234234)
func(x)