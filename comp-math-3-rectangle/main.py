import rectangle_methods as rm
import functions

functions.print_functions()

fn = int(input("Номер функции: "))
a = float(input("Левая граница: "))
b = float(input("Правая граница: "))
step = float(input("Шаг: "))

left = rm.solve_left(a,b,functions.get_function(fn),step)
mid = rm.solve_mid(a,b,functions.get_function(fn),step)
right = rm.solve_right(a,b,functions.get_function(fn),step)

print(f"""
    • Метод левых прямоугольников: {left}
    • Метод средних прямоугольников: {mid}
    • Метод правых прямоугольников: {right}
      """)