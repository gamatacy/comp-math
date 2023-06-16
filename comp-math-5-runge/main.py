import runge_kutta
import graph_drawer
import numpy as np
import functions

functions.print_functions()
n = int(input("Номер функции: "))
f = functions.get_function(n)
x0 = float(input("x начальное значение: "))
y0 = float(input("y начальное значение: "))
x_end = float(input("x конечное значение: "))
h = float(input("Шаг: "))

x, y = runge_kutta.solve(x0, y0, x_end, h, f)
graph_drawer.draw(x,y)
