def create_adder(x):
    def adder(y):
        return x + y
    return adder

def varargs(*args):
    return args


def keyword_args(**kwargs):
    return kwargs


def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)

# When calling functions, you can do the opposite of args/kwargs!
# Use * to expand tuples and use ** to expand kwargs.
args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
all_the_args(*args)            # equivalent to all_the_args(1, 2, 3, 4)
all_the_args(**kwargs)         # equivalent to all_the_args(a=3, b=4)
all_the_args(*args, **kwargs)  # equivalent to all_the_args(1, 2, 3, 4, a=3, b=4)

add_10 = create_adder(10)
print(add_10)
res = add_10(3)   # => 13
print(res)