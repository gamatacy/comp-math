from scipy.misc import derivative
from numpy import linspace
import math

def calculate_coefficient(a, b, accuracy, func, max_len=10000):
    len_of_xarr = int(1 / accuracy)
    if len_of_xarr > max_len:
        len_of_xarr = max_len

    xarr = linspace(a, b, len_of_xarr)

    maximum = derivative(func, xarr[0])
    for x in xarr:
        der = derivative(func, x)
        if math.fabs(maximum) < math.fabs(der):
            maximum = der

    coefficient = -(1 / maximum)
    return coefficient

def solve(func, a, b, accuracy=1e-5):
    try:
        coefficient = calculate_coefficient(a, b, accuracy, func)
    except ValueError:
        raise ValueError("Cannot use simple iterations method, because cannot find derivation on this interval.")

    def sequence_func(t):
        return t + coefficient * func(t)

    x = a
    x0 = math.fabs(x) + accuracy + 1  

    steps = 0
    while math.fabs(x - x0) > accuracy:
        steps += 1
        x0 = x
        x = sequence_func(x0)

    return x