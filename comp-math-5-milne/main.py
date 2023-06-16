import milne_method
import graph_drawer
import functions

functions.print_functions()
n = int(input("Номер функции: "))
f = functions.get_function(n)
a = float(input("a: "))
b = float(input("b: "))
y0 = float(input("y0: "))
h = float(input("Шаг: "))

x,y = milne_method.solve(f, a, b, y0, h)
graph_drawer.draw(x,y)
