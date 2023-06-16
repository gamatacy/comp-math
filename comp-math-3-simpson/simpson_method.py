
def calculate_integral(a, b, f, epsilon):
    n = int((b - a) / epsilon)
    w = (b - a) / n
    integral = 0
    for i in range(n):
        x1 = a + i * w
        x2 = a + (i + 1) * w

        try:
            integral += (x2 - x1) / 6.0 * (f(x1) + 4.0 * f(0.5 * (x1 + x2)) + f(x2))
        except:
            if i == 0:
                raise ValueError("Integrated function has discontinuity or does not defined in current interval")
            pass

    return integral