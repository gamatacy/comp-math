
def solve(func,a,b, eps=1e-6, max_iterations = 1000):  
    if func(a) * func(b) >= 0:
        raise ValueError("Функция должна менять знак на заданном интервале")

    root = None
    iterations = 0

    while abs(b - a) > eps and iterations < max_iterations:
        c = (a + b) / 2

        f_c = func(c)

        if f_c == 0:
            root = c
            break
        elif func(a) * f_c < 0:
            b = c
        else:
            a = c

        iterations += 1

    root = (a + b) / 2 if root is None else root

    return root