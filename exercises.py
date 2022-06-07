from itertools import accumulate, combinations, groupby, permutations, product
import random
import secrets
import sys
from collections import Counter, deque
import logging

# lists

mylist = ["apple", "banana"]

mylist_cpy = mylist[:]
mylidt_rev = mylist[::-1]

print(mylist)
print(mylist_cpy)
print(mylidt_rev)

# tuples

mytuple_single = ("One",)

mytuple = ("Max", 28, "Boston")
if "Max" in mytuple:
    print("Yes")
else:
    print("No")

tuple_list_size = [0,1,2,"hello", True]
tuple_tuple_size = (0,1,2,"hello", True)

print(sys.getsizeof(tuple_list_size))
print(sys.getsizeof(tuple_tuple_size))

# dictionaries

mydict = {"name":"Max", "email":"max@xyz.com"}
update_dict = {"age": 25}

mydict.update(update_dict)
print(mydict)

for key, value in mydict.items():
    print(key, value)

# sets

myset = {1,1,2,3}

odd = {1,3,5,7,9}
even = {2,4,6,8}
prime = {2,3,5,7}

print(odd.union(prime))
print(even.intersection(prime))
print(prime.symmetric_difference(even))
print(even.isdisjoint(odd))

# strings

my_string = "Hello World"

print(my_string[:-1])

whitespace_string = "     hello   "
print(whitespace_string.strip())

split_string = my_string.split()
print(split_string)

print(" ".join(split_string))

string_var = 10

print(f'The number is {string_var}')

# collections

col_a = "aaabccccc"

counter = Counter(col_a)

print(counter)
print("Most common:", counter.most_common(1))

col_d = deque()

col_d.append(1)
col_d.appendleft(2)

print(col_d.pop())
print(col_d.popleft())

# itertools

iter_a = [1,2]
iter_b = [3,4]
iter_c = [1,2,3,4]

print(list(product(iter_a, iter_b)))
print(list(permutations(iter_c, 2)))
print(list(combinations(iter_c, 2)))

print(list(accumulate(iter_c, lambda x,y: x*y)))

for key, val in groupby(iter_c, key=lambda x: x%2==0):
    print(key, list(val))

# lambda functions

add5 = lambda x: x + 5

mult = lambda x,y: x*y

print(sorted([(1,2), (4,1), (2,2), (6,0)], key=lambda x: x[0]*x[1]))

# exceptions and errors

class TooBigError(Exception):
    pass

try:
    x = 50
    if x > 25:
        raise TooBigError("Too Big Error")
except TooBigError as e:
    print(e)


logging.warning("Warning message")

logger = logging.getLogger("test-logger")

logger.warning("Warning message")

# random numbers

print(random.random())
print(random.randint(0,10))
print(random.sample(mylist,1))
print(secrets.randbelow(10))
print(secrets.randbits(4))
print(secrets.choice(mylist))

# decorators

def decorator(func):
    def wrapper(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print("end")
        return result
    return wrapper

@decorator
def say_hello(name):
    print(f'hello, {name}')

say_hello("John")

# generator

def countdown(num):
    while num > 0:
        yield num
        num -= 1

cd = countdown(3)

for i in cd:
    print(i)

# function arguments

def add_all_args(*arg):
    sum = 0 
    for i in arg:
        sum += i
    return sum

print(add_all_args())
print(add_all_args(1))
print(add_all_args(1,2,3))

# * operator

print(add_all_args(*iter_c))

rep_list_items = [1]*30
print(rep_list_items)


def require_kw(a,b,*,c):
    print(a,b,c)

require_kw(1,2,c=3)

first, *end = rep_list_items
print(first)
print(end)