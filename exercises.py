# lists

import json

li = [1, 2, 4, 3]  # mutable
other_li = [4, 5, 6]
li[-1]  # last element
li[::-1]  # li[start:end:step]
li2 = li[:]  # one layer deep copy using slices (li2 is li returns False)
del li[2]  # remove element at specified index
li.remove(3)  # removes element of value from list
li.append(3)
li + other_li  # no modification
li.extend(other_li)  # modification

# tuples

tup = (1, 2, 3)  # immutable
type((1,))  # class 'tuple'; requires , when length 1
tup + (4, 5, 6)  # most list operations available for tuples
a, b, c = (1, 2, 3)  # unpacking tuples into variables
a, *b, c = (1, 2, 3, 4)
# extended unpacking: a = 1, *b = [2, 3], c = 4
d, e, f = 4, 5, 6  # tuple default creation

# dicitonary

empty_dict = {}  # dict = {"key": value}
filled_dict = {"one": 1, "two": 2, "three": 3}
valid_dict = {(1, 2, 3): [1, 2, 3]}  # keys must be immutable
# immutable: ints, floats, strings, tuples
filled_dict["one"]  # using key "one", return value pair
filled_dict.keys()  # lists all keys from dict
filled_dict.values()  # lists all values from dict
filled_dict.get("four")  # more stable than just using key "four"
# returns None, or 2nd arg
filled_dict.setdefault("five", 5)  # key "five" set to value 5
# inserts key-value pair iff pair didn't exist before
filled_dict["four"] = 4  # add new key-value pair
# also: <dict>.update({key: value})

# sets

empty_set = set()  # mutable, like mathematical sets
some_set = {1, 1, 2, 2, 3, 4}  # sets cannot have duplicate values
# some_set = {1, 2, 3, 4}
valid_set = {(1,), 1}  # elements of set must be immutable
filled_set = some_set
filled_set.add(5)  # add new elements given it doesn't exist
# set operations:
# intersection '&' : all shared elements between sets
# union '|' : all unique elements from both sets
# difference '-' : all unique elements from a not in b
# symmetric difference '^' : all unique elements in only one set
# superset '>=' : if all elements in b are in a
# subset '<=' : if all elements in a are in b

# loops

animals = ["dog", "cat", "mouse"]

for animal in animals:
    print("{} is a mammal".format(animal))  # format() interpolates
    # formatted strings

for i in range(4, 8, 2):  # range(lower, upper, step), upper exclusive
    print(i)

for idx, value in enumerate(animals):
    print(idx, value)  # enumerate(iterable) returns index-value

# exception handlers

try:
    raise IndexError("This is an index error")
    # prints error code to terminal and stops
except IndexError:
    pass  # recovery statement
except (TypeError, NameError):
    pass  # multi-exceptions allowed if needed
else:
    print("All good!")  # no exceptions encountered
finally:  # always run
    print("Resource cleaning here.")

# can use with keyword instead of try/finally
with open("text.txt") as f:
    for line in f:
        print(line)
f.close()  # close file reader

contents1 = {"aa": 12, "bb": 21}
contents2 = (1, 2, 3, 4, 5, 6)
with open("text.txt", "w+") as file:  # look at mode flags for more
    file.write(str(contents1))  # writes string to file
file.close()

with open("text2.txt", "w+") as file:
    file.write(json.dumps(contents2))  # writes object to file
file.close()

with open("text.txt", "r+") as file:
    contents1 = file.read()
print(contents1)

with open("text2.txt", "r+") as file:
    contents2 = json.load(file)
print(contents2)

# iterables
