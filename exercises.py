# lists

import json
from functools import wraps

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
    print("{} is a mammal".format(animal))
    # format() interpolates formatted strings

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
file.close()

with open("text2.txt", "r+") as file:
    contents2 = json.load(file)
print(contents2)
file.close()

# iterables

iterable = filled_dict.keys()  # keys() implements Iterable class
iterator = iter(iterable)  # iterable objects can create iterators
next(iterator)  # traversing only by references
# implicitly, for loops work for iterators
list(iterable)  # returns all elements in the iterable
list(iterator)  # returns [] because the state is saved (remaining next)

# functions


def func_arg(*args, **kwargs):
    print("Positional:", args)  # positional arguments, in order
    print("Keywords:", kwargs)  # keyword arguments, explicit assignment
    # keyword arguments must be after positional arguments


func_arg(1, 3, hello="hi")
# args are tuples, kwargs are dictionaries

tup = (1, 2, 3, 4)
dic = {"a": 3, "b": 4}
func_arg(*tup, **dic)  # * and ** expands tuples and dictionaries respectively


def adder_new(x):
    def adder(y):
        return x + y
    return adder


add_10 = adder_new(10)  # addresses x variable
print(add_10(3))  # addresses y variable

# anonymous functions

(lambda x: x > 2)(3)  # note format: second () includes argument
(lambda x, y: x ** 2 + y ** 2)(y=2, x=1)  # kwargs also works

list(map(add_10, [1, 2, 3]))  # applies function to 2nd args
# shows result as list
list(filter(lambda x: x > 5, [3, 4, 5, 6, 7]))
# filters out args using lambda function

# list comprehensions
[add_10(i) for i in [1, 2, 3]]  # each i from list, pass through add_10
[x for x in [3, 4, 5, 6, 7] if x > 5]  # list all x > 5 from list

# list comprehensions for set and dict variables
{x for x in 'abcddeef' if x not in 'abc'}  # set comprehension
{x: x**2 for x in range(5)}  # key-value pair where keys go from 0-4

# generators
# returns iterator object with sequence of values
# 'yield' keyword used instead of 'return'
# memory efficient


def double_numbers(iterable):
    for i in iterable:
        yield i + i
# each number in iterable, double its value and add it to an
# internal iterable object (list maybe?)


for i in double_numbers(range(1, 900000000)):
    print(i)
    if i >= 30:
        break

# generator comprehensions, can be typed to list
values = (-x for x in [1, 2, 3, 4, 5])
for x in values:
    print(x)

# decorators
# 'beg' func wraps 'say' func
# use '@' to define the decorator function, which dynamically
# alter functionality of function, method or class without
# using subclasses or changing source code of decorated function


def beg(target_function):
    @wraps(target_function)
    def wrapper(*args, **kwargs):
        msg, say_please = target_function(*args, **kwargs)
        if say_please:
            return "{} {}".format(msg, "Please! I am poor :(")
        return msg
    return wrapper


@beg
def say(say_please=False):
    msg = "Can you buy me a beer?"
    return msg, say_please


print(say())
print(say(True))
