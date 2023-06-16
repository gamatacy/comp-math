import numpy as np

def f1(x, y):
    return np.cos(x) - y

def f2(x: float, y: float):
    return np.sin(x)


def f3(x: float, y: float):
    return (x * y)/2


def f4(x: float, y: float):
    return y - (2 * x)/y


def f5(x: float, y: float):
    return x + y

def print_functions():
    print("""
    1. y' = cos(x) - y 
    2. y' = sin(x)
    3. y' = xy/2
    4. y' = y - 2x/y
    5. y' = x + y
    """)

def get_function(n):
    match n:
        case 1:
            return f1
        case 2:
            return f2
        case 3:
            return f3
        case 4:
            return f4
        case 5:
            return f5
        case _:
            pass
