import snae_functions as se
import newton_method as nm
import chord_method as cm
import tangent_method as tm

print(
"""
Решить нелинейное уравнение - введите 1
Решить систему нелинейных уравнений - введите 2
Выйти - 3
"""
)
while True:
    cmd = input("<console> ")
    match cmd:
        case "1":
            se.print_solo_functions()
            fun = se.get_function(input("Введите номер функции: "))
            a = float(input("Введите левую границу: "))
            b = float(input("Введите правую границу: "))
            chord = cm.solve(fun,a,b)
            tang = tm.solve(fun,a)
            print(f"Метод хорд: {chord}")
            print(f"Метод касательных: {tang}")
            print(f"Разница между методами: {abs(chord - tang)}")
        case "2":
            print("Выберите систему:")
            se.print_functions()
            num = int(input("Введите номер системы: "))
            x0 = float(input("Введите начальное приближение x: "))
            y0 = float(input("Введите начальное приближение y: "))
            res = nm.solve(se.get_functions(num), [x0,y0])
            print(f'x = {res[0]}, y = {res[1]}')
        case "3":
            break
        case _:
            pass
