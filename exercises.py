#wrapping a function inside of another one
def func(x):
    def func2():
        print(x)
    return func2

#*args, **kwargs arguments and keyword arguments
def another(*args, **kwargs):
    print(args, kwargs)

def t_except(a):
    try:
        x = 7/a
    except Exception as e:
        print(e)
    finally:
        #close files, cleanup & so on
        print('finally')

if __name__ == "__main__":
    x = func(3)
    x()

    ##unpacking
    x =  [1,2,3,4,5]
    print(*x)

    another(1,2,3,4,5, one=1)