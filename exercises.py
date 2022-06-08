# lists

li = [1, 2, 4, 3]  # mutable
other_li = [4, 5, 6]
li[-1]  # last element
li[::-1]  # li[start:end:step]
li2 = li[:]  # one layer deep copy using slices (li2 is li returns False)
del li[2]  # remove element at specified index
li.remove(4)  # removes element of value from list
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

empty_dict = {}
