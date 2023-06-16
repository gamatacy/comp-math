
def solve(x0, y0, x_end, h, f):
 
    n = int((x_end - x0) / h)
    
    x = [x0]
    y = [y0]
    
    for i in range(n):
    
        k1 = f(x[-1], y[-1])
        k2 = f(x[-1] + h/2, y[-1] + k1*h/2)
        k3 = f(x[-1] + h/2, y[-1] + k2*h/2)
        k4 = f(x[-1] + h, y[-1] + k3*h)
        
        y_next = y[-1] + (k1 + 2*k2 + 2*k3 + k4)/6 * h
        
        x.append(x[-1] + h)
        y.append(y_next)
        
    return x, y