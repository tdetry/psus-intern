from decimal import DivisionByZero


def arithmeticoperators(a,b):
    ls = []
    ls.append(a+b) #addition
    ls.append(a-b) #subtraction
    ls.append(a*b) #multiplication
    ls.append(a**b)# exponent
    ls.append(a/b) # division
    ls.append(a//b)#integer division
    ls.append(a%b) # modulo
    return ls
print(arithmeticoperators(1,2))
print(arithmeticoperators(1.0,3))
print(arithmeticoperators(-2,-3))
#print(arithmeticoperators(True,False)) #will throw a division by zero error as False is 0 and True is 1

def boolean_operators(a,b):
    '''
    playing around with boolean operators
    '''
    print(a and b)
    print(a or b)
    print(a or (a and b))
    print(not a and b)
boolean_operators(True,False)
boolean_operators(False,True)
boolean_operators(True,True)

def type_casting():
    '''
    Playing with typecasting'''
    print(int(5.0))
    print(int(7.3))
    print(bool(2)) # anything other than a 0 will give True
type_casting()

def comparision_operators(a,b):
    '''
    Playing with the comparision operators'''
    print(a<b)
    print(a==b)
    print(a>=b)
    print(a!=b)
    print(a and b)
comparision_operators(5,6)
comparision_operators(True,False)

def is_vs_equal():
    '''
        palying with equal and is operators'''
    a = ['a']
    b=a
    print(a is b)
    print(a ==b)
    b = ['a']
    print(a is b)
    print(a == b)
    pass
is_vs_equal()

def string_manipulations(s):
    '''
    '''
    try:
        s[1] = 4
    except:
        print("Strings are immutable and cannot be changed")
    s  =s+s 
    print(s) # string concatinations are possible, it will technically add these two strings and will replace s with the result, hence it is not modifying the string but replacing it.
    print(len(s))
    print(s[1])
string_manipulations('a')

def list_manipulations(ls):
    '''
    Key points lists are non homogenous and can store values of different types'''
    if ls:
        ls.pop(-1)
    ls.append(3)
    ls.append('a')
    ls.append(2.0)
    # different slicing 
    print(ls[1:])
    print(ls[:])
    print(ls[::-1])
    print(ls[-3:-1])
    ls.remove(3)# remove first occurence of 3

    
    ls.append(3)
    ls.index(3) # get the index of first occurence of 3
    print(ls+ls)
    
    return ls
print(list_manipulations([]))

# Tuples are similar to lists but they are immutable. Hence once created they cannot be modified.
def dict_manipulations():
    ''''''
    m = {}
    m['a'] = 1
    # We can only use immutable data types as keys in dict
    m['b'] =2
    print(list(m.keys())) # will retrieve all the keys in the dict and will convert it into list
    print(list(m.values())) # will retrieve all the values in the dict and will convert them into a list
    # to check if an element is in the dict. we can do 
    if 'a' in m :
        print('a is a key in the dict')
    # we can get the values of dict in the following ways.
    print(m['a'])
    print(m.get('a'))
dict_manipulations()

def set_manipulations():
    s = set()
    # sets can only hold immutable data
    s.add(5)
    s.add(6)
    print(s)
    # set operations like intersection,union , ifference can we performed
    b = {2,3,5}
    print(s-b) # this will only give the elements which are there in s but not in b
    print(s^b) # this is symmetric difference
    print(s&b)
    print(s|b)
set_manipulations()

def control_flows_and_iterables():
    '''
        '''
    a = 5
    if a>5:
        print('a is greater than 5')
    elif a <5:
        print('a is less than 5')
    else:
        print('a is 5')
    # lsit iterations can be used using the for look
    for x in ['a',5,'v']:
        print(x)
    # we can use the range iterable for iterating over numbers
    for i in range(5):
        if i ==1:
            break
    # we can use enumerate in order to retrieve both the index and the value at the index
    for i,x in enumerate(['a','b','c']):
        print('index', i,'value',x)

    i = 5 
    while i < 5:
        i+=1
control_flows_and_iterables()    

def exception_handling():
    '''
    '''
    try:
        raise DivisionByZero('error')
    except DivisionByZero as e:
        print(e.args)
    else:
        print('will reach here only if there is ni error')
    finally:
        print('will reach here no matter what happens')
exception_handling()
def file_handling():
    '''
    '''
    # open file
    with open('example.txt') as f :
        contents = f.read()
        print(contents)
    # similarly write will work
def variable_arguments(*args,** kwargs):
    '''
    This finction takes variable arguments and stores in a tuple. we can also sent keyword arguements using the ** operator it stores them as a dict
    '''
    print(args)
    print(kwargs)
variable_arguments(1,3,4)
# we can use the global variable 
        


class Student:
    name = 'unknown' # class attribute
    age = 'unknown'
    def __init__(self):
        self.age = 20  # instance attribute

    @classmethod
    def tostring(cls):
        print('Student Class Attributes: name=',cls.name,', age=', cls.age)

    @staticmethod
    def static_method():
        print('this is a static method')
    @property
    def get_age(self):
        return self.age
s = Student()
#class method can only access class attributes and not all methods
print(s.tostring())

#static methods can be called with the class name or the object name
print(Student.static_method())

# Inheritence 
class Shape :
    def __init__(self,name) -> None:
        self.name =name
    def area(self):
        return 'not implemented'
    
class Square(Shape):
    def __init__(self,side) -> None:
        super().__init__('square')
        self.side = side
    def area(self):
        return self.side**2
    def perimeter(self):
        return self.side*4

s = Square(5)
print(s.name)
print(s.area())

#generators are used for lazy loading. This will help in not loading all the data at once rather loading only the value which is required at that point of time.

# decorators are way to change or modify the functionality of a function without changing the actual code.
# each function is an object and can be passed to another function as parameter.
# wrapper 
def f1(func):
    def wrapper():
        print("Started")
        func()
        print("ended")
    return wrapper
def f():
    print('Hello')
f1(f)()
f =f1(f)
f()
@f1
def f2():
    print("hi")
f2()