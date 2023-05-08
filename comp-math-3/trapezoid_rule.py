def calculate_integral(a, b, fun, epsilon):
    n = int((abs(a) + abs(b)) // epsilon)
    h = (b - a) / n
    s = 0
        
    try:
        s = 0.5 * (fun(a) + fun(b)) * h
    except:
        return [False,"Отрезок не подходит под ОДЗ"]
    
    for i in range(1, n):
        x = a + i * h
        try:
            s += fun(x)
        except:
            pass
    return [True,h * s]

