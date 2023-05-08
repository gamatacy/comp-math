def create_jacobi_matrix(f1,f2, x=[0,0]):
    h = 0.00001
    
    m = [
        [(f1([x[0] + h, x[1]]) - f1([x[0], x[1]])) / h,
        (f1([x[0], x[1] + h]) - f1([x[0], x[1]])) / h],
        [(f2([x[0] + h, x[1]]) - f2([x[0], x[1]])) / h,
        (f2([x[0], x[1] + h]) - f2([x[0], x[1]])) / h]
    ]
    
    return m
    
def solve(funcs, start, eps=1e-5):
    f1 = funcs[0]
    f2 = funcs[1]
    x0 = start[0]
    y0 = start[1]
    while True:
        f1x0 = f1([x0, y0])
        f2x0 = f2([x0, y0])
        
        jac = create_jacobi_matrix(f1,f2,[x0,y0])
        
        det = jac[0][0]*jac[1][1] - jac[0][1]*jac[1][0]
        if det == 0:
            raise ValueError("Метод Ньютона неприменим")
        dx, dy = (jac[1][1]*f1x0 - jac[0][1]*f2x0)/det, (-jac[1][0]*f1x0 + jac[0][0]*f2x0)/det

        x1, y1 = x0 - dx, y0 - dy

        if abs(x1 - x0) < eps and abs(y1 - y0) < eps:
            break
            
        x0, y0 = x1, y1
        
    return [x0,y0]
    
