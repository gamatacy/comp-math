import gauss_method as gm
import matrix_generator as mg
import file_reader as fr
import user_input as ui

print("""
      input - ввод через консоль
      random - случайная матрица
      file - ввод из файла
      
      """)

while (True):
    cmd = input("console>")
    matrix = []
    match cmd:
        case "random":
            try:
                size = int(input("Введите размер матрицы: "))
                matrix = mg.generate_random_matrix(size)
            except:
                print("Введите целое число!")
                continue
        case "file":
            try:
                path = input("Введите путь до файла: ")
                matrix = fr.read(path)
            except Exception as e:
                print(e)
                continue
        case "input":
            try:
                matrix = ui.read_matrix()
            except:
                print("Error occured")
                continue
        case _:
            break

    b = []
    n = len(matrix)
    for i in range(n):
        b.append(matrix[i][n])
    print("Исходная матрица:")
    gm.print_matrix(matrix,b)
            
    try:
        x, r, t, d = gm.solve(len(matrix),matrix)
        gm.print_answer(x,r,t,d)
    except Exception as e:
        print(e)
