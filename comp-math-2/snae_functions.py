import math

k = 0.4
a = 0.9

def first_function(args: []) -> float:
    return math.sin(args[0])

def second_function(args: []) -> float:
    return (args[0] * args[1]) / 2

def third_function(args: []) -> float:
    return math.tan(args[0]*args[1] + k) - pow(args[0], 2)

def fourth_function(args: []) -> float:
    return a * pow(args[0], 2) + 2 * pow(args[1], 2) - 1

def default_function(args: []) -> float:
    return 0.0

def print_functions():
    print("\033[94m=== 1 system ===")
    print("sin(x)")
    print("x * y / 2")
    print("================\n")
    print("=== 2 system ===")
    print("tan(x*y + 0.4) - x^2")
    print("0.9 * x^2 + 2 * y^2 - 1")
    print("================\n")
    print("=== 3 system ===")
    print("tan(x*y) - x^2")
    print("0.5 * x^2 + 2 * y^2 - 1")
    print("================\n")
    

def solo_first_function(x):
    return 2 * x ** 4 - 3 * x ** 3 - 5 * x ** 2 - 8 * x

def solo_second_function(x):
    return x ** 3 - 2 * x + 6

def solo_third_function(x):
    return math.log(x,math.e) + (x + 1) ** 3

def print_solo_functions():
    print("\033[94m=== 1 function ===")
    print("2x^4 - 3x^3 - 5x^2 - 8x = 0")
    print("================\n")
    print("=== 2 function ===")
    print("x^3 - 2x + 6 = 0")
    print("================\n")
    print("=== 3 function ===")
    print("ln(x) + (x + 1)^3 = 0")
    print("================\n")

def get_function(n):
    match n:
        case "1":
            return solo_first_function
        case "2":
            return solo_second_function
        case "3":
            return solo_third_function

def get_functions(n: int):
    if n == 1:
        return [first_function, second_function]
    elif n == 2:
        k = 0.4
        a = 0.9
        return [third_function, fourth_function]
    elif n == 3:
        k = 0
        a = 0.5
        return [third_function, fourth_function]
    else:
        return [default_function]
