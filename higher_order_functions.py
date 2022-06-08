def inc(x):
    return x+1

def dec(x):
    return x-1

def operation(func,x):
    res = func(x)
    return res

print(operation(inc,1))
print(operation(dec,1))

def is_called():
    def is_returned():
        print("Hello")
    return is_returned


new = is_called()

# Outputs "Hello"
new()