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
    m = {}
    m['a'] = 1
    # We can only use immutable data types as keys in dict
