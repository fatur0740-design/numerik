import math

# Fungsi
def f(x):
    return x - math.cos(x)

# Turunan fungsi
def df(x):
    return 1 + math.sin(x)

# Metode Newton–Raphson
def newton_raphson(x0, tol=1e-6, max_iter=50):
    for i in range(max_iter):
        fx = f(x0)
        dfx = df(x0)

        if dfx == 0:
            print("Turunan nol, metode gagal.")
            return None

        x1 = x0 - fx / dfx

        print(f"Iterasi {i+1}: x = {x1}, f(x) = {f(x1)}")

        if abs(f(x1)) < tol:
            return x1

        x0 = x1

    return x1

# ---- Eksekusi ----
akar = newton_raphson(0.5)   # tebakan awal
print("Akar ditemukan:", akar)