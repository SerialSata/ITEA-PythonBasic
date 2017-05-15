# import test_package.module1
# print(test_package.module1.a)
# import random
#  help(random.randint)
# dir(random)

# ========================================
# a = 4
# def set_a(x):
#     global a
#     a=x
#     return "now a is 8"
# print(a)
# print(set_a(8))
# print(a)

# ========================================
# def max_(x, y):
#     """ return max value
#     >>>max_(2,3)
#     3
#     >>>max_(3,2)
#     3
#     >>>max_(3,3)
#     'even'
#     """
#     if x>y:
#         return x
#     elif y>x:
#         return y
#     else:
#         return 'even'
# запустить из консоли python3.6 -m doctest "lect 5 work.py" -v

# ========================================

def add(x,y):
    '''return summ of x and y
    >>> add(2, 3)
    5
    '''
    return x + y

def minus(x,y):
    '''return x minus y
    >>> minus(6, 3)
    3
    '''
    return x - y

def compose(x,y):
    '''return compose of x and y
    >>> compose(2, 3)
    6
    '''
    return x * y

def divide(x,y):
    '''return x divide y
    >>> divide(6, 3)
    2.0
    '''
    return x / y

def calculate():
    '''Calculate x "operand" y'''
    while True:
        value1 = float(input('Input first value: '))
        value2 = float(input('Input second value: '))
        operand = str(input('What do you want to do? \nYou can +, -, *, / or "q" to quit. Make a choice: '))

        if  operand == "+":
            return add(value1, value2)
        elif operand == "-":
            return minus(value1, value2)
        elif operand == "*":
            return compose(value1, value2)
        elif operand == "/":
            return divide(value1, value2)
        elif operand == "q":
            return 'Goodbye!'

print(calculate())


