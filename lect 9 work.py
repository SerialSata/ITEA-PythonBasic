def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

# print(fact(20))

def f(n):
    def g(x):
        return n * x
    return g
double = f(2)
triple = f(3)
quadruple = f(4)

# print(double(2), triple(2), quadruple(2))

def double_(x):
    return 2 * x
# print(list(map(double, ['aa', 'bb', 'cc'])))

def odd(x):
    return x % 2
# print(list(filter(odd, [1, 2, 3, 4, 5])))

import functools
def add(x, y):
    return x + y
# print(functools.reduce(add, [1,2,3,4,5]))

# print(list(map(lambda x: 2*x, [1,2,3,4])))

# print(functools.reduce(lambda a, x: x, [1,2,3,4]))


def f(*args, **kwargs):
    print(args, kwargs)
# print(f('f', 'a', a=2, b=7, c=9))

def calc_price(price, *, kg=None, g=None):
    if g and kg:
        raise ValueError
    if g is not None:
        kg= g/1000
    return kg * price
# print(calc_price(5, g=800))

t=1,2,3
d={'a':3, 'b':4, 'c':5}
def f(a,b,c):
    return a+b+c
# print(f(*t))
# print(f(**d))
# print(f(*d))

# print(list(zip([1,2,3], [4,5,6])))

m = [
     [1,2,3],
     [4,5,6],
     [7,8,9]
     ]
# print(list(zip(*m)))

def get_area(x):
    return x*x

def scale(f):
    def wrapper(x):
        print("I'm wrapping it")
        res = f(x*100)
        print('Out of wrapper')
        return res
    return wrapper

# get_area = scale(get_area)
# print(get_area(5))

@scale
@scale
def get_area(x):
    return x*x

# print(get_area(5))

def log(f):
    print('in log')
    def wrapper(*args, **kwargs):
        print('Params', args, kwargs)
        res = f(*args, **kwargs)
        print('result', res)
        return res
    print('out log')
    return wrapper

@log
def add(x,y):
    return x+y

print(add(2,3))