import numpy as np

def generate_points(n,f):
    x = np.linspace(f[1],f[2], n)
    y = f[0](x)
    return x, y