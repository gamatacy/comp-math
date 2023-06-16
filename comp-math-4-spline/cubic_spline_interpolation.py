def cubic_spline_interpolation(x, y):
    n = len(x)
    h = list(map(lambda i: x[i + 1] - x[i], range(n - 1)))
    b = [0] * n
    u = [0] * n
    v = [0] * n
    z = [0] * n
    alpha = list(map(lambda i: 3 * (y[i + 1] - y[i]) / h[i] - 3 * (y[i] - y[i - 1]) / h[i - 1], range(1, n - 1)))
    for i in range(1, n - 1):
        l = 2 * (x[i + 1] - x[i - 1]) - h[i - 1] * u[i - 1]
        u[i] = h[i] / l
        b[i] = (alpha[i - 1] - h[i - 1] * b[i - 1]) / l
    for i in range(n - 2, 0, -1):
        z[i] = b[i] - u[i] * z[i + 1]
    coefficients = []
    for i in range(n - 1):
        a = y[i]
        b = (y[i + 1] - y[i]) / h[i] - h[i] * (z[i + 1] + 2 * z[i]) / 3
        c = z[i]
        d = (z[i + 1] - z[i]) / (3 * h[i])
        coefficients.append((a, b, c, d))
    return coefficients

def solve(x, y, xi):
    coefficients = cubic_spline_interpolation(x,y)
    index = next((i for i, val in enumerate(x[:-1]) if val <= xi <= x[i + 1]), None)
    if index is not None:
        a, b, c, d = coefficients[index]
        dx = xi - x[index]
        return a + b * dx + c * dx**2 + d * dx**3