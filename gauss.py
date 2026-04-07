def gauss_elimination(A, b):
    n = len(A)

    # Forward Elimination
    for i in range(n):
        # Pivoting
        if A[i][i] == 0:
            for j in range(i+1, n):
                if A[j][i] != 0:
                    A[i], A[j] = A[j], A[i]
                    b[i], b[j] = b[j], b[i]
                    break

        # Eliminasi
        for j in range(i+1, n):
            rasio = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= rasio * A[i][k]
            b[j] -= rasio * b[i]

    # Back Substitution
    x = [0]*n
    for i in range(n-1, -1, -1):
        jumlah = sum(A[i][j] * x[j] for j in range(i+1, n))
        x[i] = (b[i] - jumlah) / A[i][i]

    return x


# Contoh pemakaian
A = [[2, 1, -1],
     [-3, -1, 2],
     [-2, 1, 2]]
b = [8, -11, -3]

print("Hasil:", gauss_elimination(A, b))