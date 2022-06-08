#User-Inputting

# name = input("Please Enter your name")

# print ("Your Name is", name)

# type conversion of input

# inp = input("Enter something: ")
# print ("The typeof", type(inp), 'value', inp)
# inp = int(inp)
# print ("The type of input after conversion", type(inp), 'value', inp)

#Arithematic operations

x = 9
y = 15 

print ('The sum is:', x + y)

#division

print ("Division of 4 by 2 gives us(float)", 4/2)

# print out an integer after division

print ("Division of 4 by 2 gives us(int)", 4//2)


#string operations

hello = 'hello'

print ("uppercase: ", hello.upper() )

print (" LowerCase: ", hello.lower() )

print ("Capitalise the first alphabet", hello.capitalize() )

print ( (hello + ' ')* 3 )


#conditional operators

print ('a' > 'Z')

print (ord('Z'))

print (ord('a'))

# chained operations

x = 5
y = 10
z= 8

r1 = x==y
r2 = y > x
r3 = z < x + 2

# x = int(input ("Age: "))

# if (x > 18) :
#     print ("You are old enough to drive")
# elif (x== 18):
#     print ("You can drive now")
# else:
#     print ("You are too young to drive")



# lists in python

temp = [1, 2, 3, 4]
print ("Len of temp", len(temp))

temp.append(5)

print ("len of Temp after appending", len(temp))

# extending a list

temp.extend([6, 7, 8, 9])

print ("Temp after extending", temp)

# copying a list versus referencing a list

x = [4, True, 'Hello']
# here y refer to the list 
y = x
# copies the list
z = x[:]

print ('The list of x: ', x)

x[0] = "Hi"

print ('The list of x: ', x, "The list of y: ", y, "The list of z:", z)

# Tuples in python

tup = (1, 2, 3, 4, 5)

print ("The tuple t is: ", tup)

# they are immutable and cannot be changed

for i in range (10):
    print ("i: ", i)

for i in range (10, 1, -1):
    print ("i: ", i)

for i in x:
    print ("items in x", i)

#slicing in python

x = [1, 2, 3, 4, 5, 6, 7, 8]

print ("From index 2 to till the end", x[2:])
print ("Skiping one element from the begining till the end", x[::2])
print ("reverse a list", x[:: -1])
print ("skiping one element from the end", x[::-2] )

# sets in python

s = set()

s.add(1)
s.add(3)
s.add(4)
s.add(5)

print ("The set s is: ", s)

print ("checking is 2 is in s", 2 in s)

print ("adding 2 to s", s.add(2))

print ("removing 1 from the set", s.remove(1))

print ("The updated set is: ", s)

# dicts

x = {}

x['key1'] = "one"
x['key2'] = "Two"

# iterating all the keys

for k in x.keys() :
    print ("Keys: ", k)

print ("converting the keys to a list", list(x.keys()) )

for val in x.values() :
    print ("Values", val)

print ("Converting the values to a list", list(x.values() ) )

for key, value in x.items():
    print ("The key is", key, "The value is", value)

#comprehensions

x= [i for i in range(10)]

print ("the list x is :", x)

x= [[i for i in range(5)] for i in range(10) ]

print ("the list x is :", x)

# functions

def func():
    print ("a new function")


def func2(x, y):
    def func3():
        print ("The value of x and y is: ", x, y)
    return func3
#func2(3)()

# *args and *kwargs

def func_Args(*args):
    for arg in args:
        print ("Arguments passed", arg)

def func_Kwargs(it, **kwargs):
    print ("first argument", it)
    for key, value in kwargs.items() :
        print (" The key is %s the value is %s" %(key, value) )

func_Args("Welcome", "To", "Odoo")

func_Kwargs("Item One", First=" Welcome", Middle = "To", Last="Odoo" )

# handling exceptions

try:
    x = 7 / 0
except Exception as e :
    print (e)
finally:
    print ('Closing the Program Unable to perform operation')

# lambda functions

addTwoNumbers = lambda a, b : a + b

print(addTwoNumbers(2, 3))

# map and filter function

x = [1, 2, 3, 4, 5]

x_1 = map( lambda i: i * 2, x )

print ('mapped function', list(x_1) )

x_2 = filter( lambda i: i % 2 == 0, x)

print ("Filtered List only multiples of 2", list(x_2))

def new_Write(x):
    return x + 5

x_3 = map(  new_Write , x )

print ("mapping with a new function", list(x_3) )

# F Strings

age = 23

x = f'You are {age} years old'

print (x)


#Decorators


def function1( fun):
    def wrapper(*args, **kwargs):
        print ("Starts")
        val = fun(*args, **kwargs)
        print ("Ends")
        return val
    return wrapper

@function1
def function2 (name):
    print ("Hello", name)
    return "Hi!, " + name

# function1(function2)()

out = function2("Ranjeet")

print("This is the output: ", out)
