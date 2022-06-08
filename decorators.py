#Decorators

#OLD SCHOOL Way

def bread(func):
    def wrapper(*args):
        print('Bread')
        veggies(*args)
        print('Bread')

    return wrapper


def veggies(*args):
    print([*args])


makeSandwich = bread(veggies)
makeSandwich('lettuce', 'tomato', 'onion', 'cucumber','mayo', 'chipotle')

#The Cool Way

def veggie(func):
    # print(*args)
    def wrapper(pty,veg):
        print("BREAD")
        print('------')

        print(veg)
        func(pty)
        print('------')
        print("BREAD")
    return wrapper

@veggie
def patty(pty):
    print([pty])


patty("Black-bean",["lettuce","onion", "cucumber", "tomato", "mayo", "chipotle"])