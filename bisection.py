# Metode Bisection untuk persamaan linear f(x) = a*x + b

def f(x):
    a = 2   # ubah sesuai koefisien linear
    b = -4  # ubah sesuai konstanta
    return a * x + b

def bisection(a_interval, b_interval, tol=1e-6, max_iter=100):
    fa = f(a_interval)
    fb = f(b_interval)

    if fa * fb > 0:
        print("Bisection gagal: f(a) dan f(b) harus berbeda tanda.")
        return None

    for i in range(max_iter):
        c = (a_interval + b_interval) / 2
        fc = f(c)

        print(f"Iterasi {i+1}: c = {c}, f(c) = {fc}")

        if abs(fc) < tol:
            return c

        if fa * fc < 0:
            b_interval = c
            fb = fc
        else:
            a_interval = c
            fa = fc

    return c

# ---- Eksekusi ----
akar = bisection(0, 5)   # interval harus mengurung akar
print("Akar ditemukan:", akar)