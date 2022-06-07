def start_end_decorator(func):
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper


# @start_end_decorator
# def print_name():
#     print('Alex')

@start_end_decorator
def add5(x):
    return x+5


add5(10)
