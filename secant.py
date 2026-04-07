import math

# Fungsi yang ingin dicari akarnya
def f(x):
    return x - math.cos(x)

# Metode Secant
def secant(x0, x1, tol=1e-6, max_iter=50):
    for i in range(max_iter):
        f0 = f(x0)
        f1 = f(x1)

        if f1 - f0 == 0:
            print("Gagal: pembagian dengan nol.")
            return None

        # Rumus metode Secant
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)

        print(f"Iterasi {i+1}: x = {x2}, f(x) = {f(x2)}")

        # Jika sudah mendekati nol
        if abs(f(x2)) < tol:
            return x2

        x0, x1 = x1, x2

    return x2

# ---- Eksekusi ----
akar = secant(0, 1)   # dua tebakan awal yang umum digunakan
print("Akar ditemukan:", akar)