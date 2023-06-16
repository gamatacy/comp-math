import trapezoid_rule as tr
import functions

functions.print_functions()

fn = int(input("Номер функции: "))
a = int(input("Левая граница: "))
b = int(input("Правая граница: "))
eps = float(input("Шаг: "))

res = tr.calculate_integral(a,b,functions.get_function(fn),eps)

if res[0]:
    print(f"Значение интеграла: {res[1]}")
else:
    print(f"{res[1]}")