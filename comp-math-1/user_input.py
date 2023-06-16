def read_matrix():
    n = int(input("Введите размер матрицы: "))
    matrix = []
    print("Введите коэффициенты и свободный член через пробел")
    for i in range(n):
        matrix.append(list(map(float, input(f"{i+1} строка: ").split())))
    return matrix