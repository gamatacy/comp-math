import matplotlib.pyplot as plt
import cubic_spline_interpolation as cs
import numpy as np

def draw(x,y):
    plt.plot(x, y, 'o', label='Исходные точки', color='red')
    
    x_new = np.linspace(x[0], x[-1], 50)
    y_new = [cs.solve(x, y, xi) for xi in x_new]

    plt.plot(x_new, y_new, '-', label='Интерполяция', color='blue')
    
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    
    plt.legend()
    plt.show()


