def jacobi(A, b, x0=None, tol=1e-6, max_iter=50):
    n = len(A)
    if x0 is None:
        x0 = [0]*n

    x = x0.copy()

    for itr in range(max_iter):
        x_new = x.copy()

        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]

        print(f"Iterasi {itr+1}: {x_new}")

        if max(abs(x_new[i] - x[i]) for i in range(n)) < tol:
            return x_new

        x = x_new

    return x


# Contoh
A = [[4, 1, 2],
     [3, 5, 1],
     [1, 1, 3]]
b = [4, 7, 3]

print("Hasil:", jacobi(A, b))