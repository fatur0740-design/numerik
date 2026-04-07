def gauss_jordan(A, b):
    n = len(A)

    for i in range(n):
        # Normalisasi pivot
        pivot = A[i][i]
        for j in range(n):
            A[i][j] /= pivot
        b[i] /= pivot

        # Eliminasi baris lain
        for k in range(n):
            if k != i:
                faktor = A[k][i]
                for j in range(n):
                    A[k][j] -= faktor * A[i][j]
                b[k] -= faktor * b[i]

    return b


# Contoh
A = [[2, 1, -1],
     [-3, -1, 2],
     [-2, 1, 2]]
b = [8, -11, -3]

print("Hasil:", gauss_jordan(A, b))