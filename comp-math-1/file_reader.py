
def read(path):
    try:
        f = open(path, 'r')
        n = int(f.readline())
        matrix = []
        for i in range(n):
            matrix.append(list(map(float, f.readline().split())))
        f.close()
        return matrix
    except:
        raise ValueError("Неправильное имя файла или формат матрицы")
    