def check(a,b,f):
    if (a <= 0 and 0 <= b or b <= 0 and 0 <= a):
        try:
            f(0)
        except:
            return False
    return True

def solve_mid(a, b, f, step):
    n = int((abs(a) + abs(b) )/ step)
    h = (b - a) / n 

    if (not check(a,b,f)): return "Integrated function has discontinuity or does not defined in current interval"
    
    try:
        integral_sum = sum(f(a + h/2 + i * h) for i in range(n))  
    except:
        pass
        
    integral = h * integral_sum 

    return integral

def solve_left(a, b, f, step):
    n = int((abs(a) + abs(b) )/ step)
    h = (b - a) / n 
    
    if (not check(a,b,f)): return "Integrated function has discontinuity or does not defined in current interval"
    
    try:
        integral_sum = sum(f(a + i * h) for i in range(n)) 
    except:
        pass
    
    integral = h * integral_sum

    return integral

def solve_right(a, b, f, step):
    n = int((abs(a) + abs(b) )/ step)
    h = (b - a) / n  

    if (not check(a,b,f)): return "Integrated function has discontinuity or does not defined in current interval"

    try:
        integral_sum = sum(f(a + (i + 1) * h) for i in range(n))  
    except:
        pass
    
    integral = h * integral_sum  

    return integral