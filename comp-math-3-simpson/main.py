import simpson_method as sm
import functions

functions.print_functions()

try:
    f = functions.get_function(int(input("Номер функции: ")))
    a = int(input("Левая граница: "))
    b = int(input("Правая граница: "))
    eps = float(input("Шаг: "))
    print(sm.calculate_integral(a,b,f,eps))
except Exception as e:
    print(e)