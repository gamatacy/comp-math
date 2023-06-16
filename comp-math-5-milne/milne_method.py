import math

def get_n(x0, xn, h):
    return int(math.ceil(round(abs(xn - x0) / h, 3)))

def runge_kutta_method(func, x0, xn, y0, h):
    x_previous = [x0]
    y_previous = [y0]
    n = get_n(x0, xn, h)
    for i in range(n):
        x_now = x_previous[i]
        y_now = y_previous[i]
        k1 = h * func(x_now, y_now)
        k2 = h * func(x_now + h / 2, y_now + k1 / 2)
        k3 = h * func(x_now + h / 2, y_now + k2 / 2)
        k4 = h * func(x_now + h, y_now + k3)
        x_previous.append(x_now + h)
        y_previous.append(y_now + (k1 + 2 * k2 + 2 * k3 + k4) / 6)
    return x_previous, y_previous


def solve(func, x0, xn, y0, h):
    n = get_n(x0, xn, h)
    if n < 5:
        return runge_kutta_method(func, x0, xn, y0, h)
    
    x_previous, y_previous = runge_kutta_method(func, x0, x0 + 3 * h, y0, h)

    x_now = x_previous[-1]
    y_now = y_previous[-1]
    f = lambda i: func(x_previous[i], y_previous[i])

    for i in range(4, n + 1):
        x_now += h

        y_now = y_previous[i - 4] + 4 * h * (2 * f(i - 3) - f(i - 2) + 2 * f(i - 1)) / 3
        y_now = y_previous[i - 2] + h * (f(i - 2) + 4 * f(i - 1) + func(x_now, y_now)) / 3

        x_previous.append(x_now)
        y_previous.append(y_now)

    return x_previous, y_previous
