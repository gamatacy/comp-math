import lagrange_interpolation as li
import graph_drawer as gd
import dots_generator as dg
import functions

functions.print_functions()

f = functions.get_function(input("Введите номер функции: "))
x_values, y_values = dg.generate_points(10,f)
print(f"Точки сгенерированы на отрезке [{f[1]}:{f[2]}]")

gd.draw(x_values, y_values) 