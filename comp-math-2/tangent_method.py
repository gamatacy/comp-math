def solve(f, x0, eps=1e-5, max_iterations = 1000, h = 0.00001):
    x = x0
    for i in range(max_iterations):
        fx = f(x)
        dfx = (f(x + h) - f(x)) / h
        if abs(fx) < eps:
            return x
        x = x - fx / dfx