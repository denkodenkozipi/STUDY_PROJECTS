def matrx(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print("Матрица A:")
for row in A:
    print(row)
print("Матрица B:")
for row in B:
    print(row)
print("Результат умножения A × B:")
result = matrx(A, B)
for row in result:
    print(row)