import random

def generate_random_matrix(size):
    matrix = []
    for _ in range(size):
        row = [random.uniform(-10, 10) for _ in range(size+1)]
        matrix.append(row)
    return matrix