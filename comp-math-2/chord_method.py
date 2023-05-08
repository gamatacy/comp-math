
def solve(f,a,b, eps=1e-6, max_iterations = 1000):  
    fa = f(a)
    fb = f(b)

    if fa * fb > 0:
        print("Метод хорд не применить: корни на заданном интервале отсутствуют")
        return 0

    i = 0
    while abs(b - a) > eps and i < max_iterations:
        x = a - (fa*(b-a))/(fb-fa)
        fx = f(x)
        if fa*fx < 0:
            b = x
            fb = fx
        else:
            a = x
            fa = fx
        i += 1
    return x