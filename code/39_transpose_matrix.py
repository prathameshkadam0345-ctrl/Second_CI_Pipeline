# Program 39: Transpose a Matrix

def transpose_matrix(matrix):
    if not matrix:
        return []

    return [list(row) for row in zip(*matrix)]
