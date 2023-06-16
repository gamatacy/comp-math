import numpy as np

def f1(x):
    return np.sin(x)

def f2(x):
    return 2 * x**2 - 3 * x + 1 

def f3(x):
    return 3 * x + 2

def get_function(n):
    match n:
        case "1":
            return [f1, 0, np.pi*2]
        case "2":
            return [f2,-3,5]
        case "3":
            return [f3,-2,4]
        case _:
            pass
        
def print_functions():
    print("""
          1. sin(x)
          2. 2x^2 - 3x + 1
          3. 3x + 2
          """)