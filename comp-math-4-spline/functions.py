import numpy as np

def f1(x):
    return np.cos(x)

def f2(x):
    return x**2 - x + 3

def f3(x):
    return 2 * x + 3

def get_function(n):
    match n:
        case "1":
            return [f1, -np.pi*2, np.pi*2]
        case "2":
            return [f2,-3,5]
        case "3":
            return [f3,-2,4]
        case _:
            pass
        
def print_functions():
    print("""
          1. cos(x)
          2. x^2 - x + 3
          3. 2x + 3
          """)