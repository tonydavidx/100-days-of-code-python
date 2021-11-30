# function with many arguments
def add(*args):
    sum = 0
    for a in args:
        sum += a

    return sum

# function with many keyword arguements


def calculate(n, **kwargs):
    add = 0
    multiply = 0
    add = n+kwargs['add']
    multiply = n*kwargs['multiply']
    print(add, multiply)


calculate(2, add=5, multiply=10)


def quiz(a, *args, **kwargs):
    print(a, args, kwargs)


quiz(4, x=1, y=2)
