def solve(n, A):
     
    b = []
    for i in range(n):
        b.append(A[i][n])
        A[i].pop()

    det = 1.0
   
    for i in range(n):
        
             
        max_row = i
        for j in range(i+1, n):
            if abs(A[j][i]) > abs(A[max_row][i]):
                max_row = j
    
        A[i], A[max_row] = A[max_row], A[i]
        b[i], b[max_row] = b[max_row], b[i]
        
        if abs(A[i][i]) < 1e-8:
            raise ValueError("The system has no roots of equations or has an infinite set of them.")

        det *= A[i][i]

        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            b[j] -= factor * b[i]
    
    triangle_matrix = [A,b]

    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - sum(A[i][j] * x[j] for j in range(i+1, n))) / A[i][i]
    
    residuals = []
    for i in range(n):
        residuals.append(b[i] - sum(A[i][j] * x[j] for j in range(n)))

    return x, residuals, triangle_matrix, det

def print_matrix(A, b):
    n = len(A)
    for i in range(n):
        row = " ".join(f"{A[i][j]:.2f}" for j in range(n))
        print(row + " | " + f"{b[i]:.2f}")

         
        
def print_answer(x,residuals,triangle_matrix, det):
    print("")
    print(f"Определитель: {det}")
    print("Треугольная матрица: ")
    print_matrix(triangle_matrix[0], triangle_matrix[1])
    print("")
    for i in range(len(x)):
        print(f"x{i+1}: {x[i]} | невязка: {residuals[i]}")