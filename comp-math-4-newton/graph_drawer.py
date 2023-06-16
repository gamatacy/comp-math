import matplotlib.pyplot as plt
import newton_method as nm
import numpy as np

def draw(x,y):
    plt.plot(x, y, 'o', label='Исходные точки')
    
    x_new = np.linspace(x[0], x[-1], 50)
    y_new = [nm.solve(x, y, xi) for xi in x_new]

    plt.plot(x_new, y_new, '-', label='Интерполяция')

    plt.legend()
    plt.show()


