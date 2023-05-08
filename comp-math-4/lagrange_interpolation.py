def solve(x_values, y_values, x):

    n = len(x_values)
    p = 0

    for i in range(n):
        basis = 1
        xi = x_values[i]
        for j in range(n):
            if j != i:
                xj = x_values[j]
                basis *= (x - xj) / (xi - xj)
        p += y_values[i] * basis
        
    return p