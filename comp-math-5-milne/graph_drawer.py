import matplotlib.pyplot as plt
import numpy as np
import lagrange_interpolation as li

def draw(x,y):

    x_new = np.linspace(x[0], x[-1], 50)
    y_new = [li.solve(x, y, xi) for xi in x_new]

    plt.plot(x, y, label='Метод Милна')
    plt.plot(x_new,y_new, "o",label='Полином Лагранжа')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
    





