def solve(x_axis, y_axis, x):
    n = len(x_axis)
    coefficients = y_axis.copy()

    for i in range(1, n):
        for j in range(n - 1, i - 1, -1):
            coefficients[j] = (coefficients[j] - coefficients[j - 1]) / (x_axis[j] - x_axis[j - i])

    result = coefficients[-1]
    for i in range(n - 2, -1, -1):
        result = result * (x - x_axis[i]) + coefficients[i]
    
    return result