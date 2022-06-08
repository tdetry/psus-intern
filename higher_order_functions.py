def inc(x):
    return x+1

def dec(x):
    return x-1

def operation(func,x):
    res = func(x)
    return res

print(operation(inc,1))

print(operation(dec,1))
