# #Python as Fast as Possible
# #Data types
# #Int
# -245788
# 7478392

# #Float
# 255.0
# -9.7

# #String
# 'hello'
# "Hello"

# #Bool
# True
# False

# #Output and printing
print('Hello world')
print(4.5)
print(4.5, 'Hello world', 'end', 87, False)

# #Variables
hello = 'tim'
world = 'world'
world = hello
hello = 'no'

# #naming conventions
hello_world = 'Hello world'

print(hello, world, hello_world)

# Inputs
name = input('Name: ')
age = input('Age: ')

print('Hello ', name, ' you are ', age, ' years old')

# #Arithmetic operators

x = 9
y = 3
result = x/y
print(result)
result = x+y
print(result)
result = x-y
print(result)
result = x//y
print(result)
result = x % y
print(result)
result = x**y
print(result)
result = (x % y) * 2

num = input('Number: ')
print(float(num)-5)

# #String methods
hello = 'hello'

print(hello.upper())
print(hello.lower())
print(hello.capitalize())
# Couunt given substrings in the string
print(hello.lower().count('ll'))

# multiply string
x = 'hello'
y = 3

print(x * y)

# concat
x = 'hello'
y = 3

print(x + y)

# #Conditional operators
x = "hello"
y = 'hello'
print(x == y)
print(x != y)
print(x > y)
print(x < y)
result = 6 == 6
print(result)

x = 7
y = 8
z = 0

result1 = x == y
result2 = y > x
result3 = z-3 < x + 2

result4 = result1 or not result2 or result3

print(result4)

# if else elif

x = input('Name: ')
if x == 'David':
    print("eres genial")

elif x == 'Joe':
    print("Bye Joe")
elif x == 'Sarah':
    print("Random")
else:
    print('no')

print("esto siempre")

# #Collections
x = [4, True, 'Hi']
x.append('hello')
print(x)
x.extend([4, 5, 5, 5, 5, 5, 5])
print(x)
print(x.pop())
print(x)
print(x[1])
x[0] = 'hello'

# Tuples
x = (0, 0, 2, 2)
# x[0]=5 cant be done
print(x[0])

# for loops
for i in [3, 2, 4, 42]:
    print(i)

for i in range(1, 10):
    print(i)
x = [3, 4, 42, 3, 2, 4]
for i in range(len(x)):
    print(x[i])

for i, element in enumerate(x):
    print(i, element)


i = 0
while i < 10:
    print('run')
    i += 1

while True:
    print('Hola')
    break

# Sliced operator
x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
y = ['hi', 'hello', 'goodbye', 'cya', 'sure']
s = 'hello'

# slicing collection[start:stop:step]

sliced = x[::-1]

print(sliced)

# Set
x = set()
s = {4, 32, 2, 2}
s2 = {3, 4, 22, 1}

print(type({}))
s.add(5)
s.remove(2)
print(s)

print(s.difference(s2))
print(s.intersection(s2))

# # Dictionaries

x = {'key': 4}
x['key2'] = 5
x[2] = [2, 2, 1, 1]
print(x)
print('key' in x)
print(list(x.values()))
print(list(x.keys()))

del x['key']
print(x)

for key, value in x.items():
    print(key, value)

# # Comprehension
x = [x+2 for x in range(5)]
print(x)

x2 = [[0 for x in range(100)] for x in range(5)]
print(x2)

x3 = [i for i in range(100) if i % 5 == 0]
x4 = {i for i in range(100) if i % 5 == 0}
x5 = tuple(i for i in range(100) if i % 5 == 0)
print(x5)

# functions


def func(x, y, z=None):
    print('Run', x, y, z)
    return x*y, x/y


r1, r2 = (func(5, 6))
print(r1, r2)

# # Unpack operator


def func(x):
    def func2():
        print(x)
    return func2


print(func(3)())


def func2(x, y):
    print(x, y)


pairs = [(1, 2), (3, 4)]

for pair in pairs:
    func2(*pair)

func2(**{'x': 2, 'y': 5})


# scope and global
x = 'tim'


def func(name):
    global x
    x = name


print(x)
func('changed')
print(x)


# # Raise Exceptions
raise Exception('Bad')
raise FileExistsError('')
# Handle Exceptions
try:
    x = 7/0

except Exception as e:
    print(e)
finally:
    print('finally')

# Lambda


def x(x, y): return x+y


print(x(2, 5))

#Map and filter

x = [1, 2, 3, 4, 5, 6, 7, 234, 1, 2, 3, 4, 5, 12, 4, 5, 5]


def func(i):
    i = i*3
    return i % 2 == 0


mp = map(lambda i: i + 2, x)
print(list(mp))
mp = filter(func, x)
print(list(mp))

# F strings
a = 9
x = f'hello {6+8} {a}'
print(x)
